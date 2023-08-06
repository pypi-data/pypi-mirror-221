"""
description: this module provides report for each step.
"""
import os
import json
import inspect
from pathlib import Path
from typing import Dict
from typing import List

from attr import asdict

from _pistar.pistar_pytest.utils import uuid4
from _pistar.utilities.condition.condition import ConditionManager
from _pistar.utilities.constants.testcase import \
    PISTAR_TESTCASE_EXECUTION_STATUS as STATUS
from _pistar.utilities.constants.testcase import STEP_TYPE
from _pistar.utilities.testcase.case import TestCase
from _pistar.utilities.constants.encode import ENCODE
from _pistar.utilities.constants.file_mode import FILE_MODE


def duration_amend(duration):
    if duration > 0:
        return duration
    else:
        return 1


def _get_post_condition_info(step_info: Dict, step_record: Dict) -> None:
    step_info['after'] = list()
    for after in step_record.get('after', []):
        after_name = list(after.keys())[0]
        result, duration = after.get(after_name)
        step_info['after'].append({
            'name': after_name,
            'result': STATUS.PASSED
            if not result else STATUS.FAILED,
            'duration': duration_amend(duration)
        })


def _get_pre_condition_info(con_manager: ConditionManager,
                            step_info: Dict,
                            step_record: Dict,
                            nodeid: str) -> None:
    step_info['before'] = list()
    conditions_result = step_record.get('before', {})
    for before in conditions_result:
        _, conditions_exception = conditions_result.get(before)

        # this is a temporary solution
        con_list = con_manager.name2confunc.get(before)
        matched = tuple(con_manager._matchfactories(con_list, nodeid))
        con = matched[-1]
        duration = con.before_end_time - con.before_start_time

        step_info['before'].append({
            'name': before,
            'result': STATUS.PASSED if not conditions_exception else STATUS.FAILED,
            'duration': duration_amend(duration)
        })


def _get_attachments(step_info: Dict, teststep: str,
                     testcase: TestCase) -> None:
    step_info['attachments'] = list()
    log_path = Path(testcase.instance.logger_path)
    testcase_filename = Path(
        inspect.getfile(testcase.clazz)
    ).stem

    last_step = list(testcase.execute_records.keys())[-1]
    if log_path.is_file() and \
            teststep == last_step:
        step_info['attachments'].append({
            'name': testcase_filename + '.log',
            'type': 'text',
            'path': str(log_path)
        })

    attaches: Dict[str, List] = getattr(testcase.instance, "_attaches", None)

    # only have teardown ,but case failed.
    if teststep == "failure" and attaches:
        if not attaches.get(teststep):
            teststep = "teardown"

    if attaches and attaches.get(teststep):
        attachments = attaches.get(teststep)
        for att in attachments:
            step_info["attachments"].append(asdict(att))


def _get_actions(step_info: Dict, teststep: str, testcase: TestCase) -> None:
    step_info['actions'] = list()
    actions = testcase.instance.action_word_information
    for action_caller in actions:
        if teststep in action_caller:
            duration_list = actions.get(action_caller)
            execute_times = len(duration_list)
            avg_duration = sum(duration_list) // execute_times
            step_info['actions'].append({
                'name': action_caller.split('.')[-1],
                'execute_times': execute_times,
                'avg_duration': duration_amend(avg_duration)
            })


def step_info_assemble(testcase: TestCase, step_info: Dict, step_record: Dict, nodeid: str, teststep: str):
    _get_pre_condition_info(
        testcase.condition_manager, step_info, step_record, nodeid)
    _get_post_condition_info(
        step_info, step_record)
    _get_attachments(step_info, teststep, testcase)
    _get_actions(step_info, teststep, testcase)


def write_report(report_path, step_info: Dict):
    with open(report_path, mode=FILE_MODE.WRITE, encoding=ENCODE.UTF8) as file:
        json.dump(step_info, file, ensure_ascii=False, default=str)


def read_report(report_path):
    with open(report_path, mode=FILE_MODE.READ, encoding=ENCODE.UTF8) as file:
        return json.load(file)


def get_step_report_info(testcase: TestCase, step_name: str):
    reports = getattr(testcase.instance, 'reports', None)
    step_record = testcase.execute_records.get(step_name)
    step_info = dict()
    if reports and step_name in reports:
        step_info['report'] = reports.get(step_name)
    step_info['name'] = step_name
    step_info['start_time'] = step_record['start_time']
    step_info['end_time'] = step_record['end_time']
    duration = step_info['end_time'] - step_info['start_time']
    step_info['duration'] = duration if duration > 0 else 1
    step_info['result'] = STATUS.PASSED if \
        step_record.get('status_code') == '0' else STATUS.FAILED
    description = getattr(getattr(testcase.instance, step_name, None), "description", step_name)
    step_info['description'] = description if description else step_name
    step_info['fullName'] = '::'.join([testcase.clazz.__name__, step_name])
    step_info['uuid'] = uuid4()
    step_info['testCaseId'] = inspect.getfile(testcase.clazz)
    if step_name == 'setup':
        step_info['step_type'] = STEP_TYPE.SETUP
    elif step_name in ['teardown', 'failure']:
        step_info['step_type'] = STEP_TYPE.TEARDOWN
    else:
        step_info['step_type'] = STEP_TYPE.TESTSTEP

    rel_path = Path(testcase.path).relative_to(Path.cwd())
    step_info['labels'] = [
        {
            'name': 'parentSuite',
            'value': str(rel_path.parent)
        },
        {
            'name': 'suite',
            'value': rel_path.name
        },
        {
            'name': 'subSuite',
            'value': testcase.clazz.__name__
        }
    ]
    nodeid = testcase.nodeid
    step_info_assemble(testcase, step_info, step_record, nodeid, step_name)
    exception = step_record.get('exception', None)
    step_info['exception'] = list()
    if exception:
        step_info['exception'].append(exception)
    return step_info


def update_last_step_condition(case: TestCase, finish_condition: List):
    steps = list(case.execute_records.keys())
    last_step = steps[-1]

    report_path_dir = case.clazz.testcase_result_path
    report_json_file = ".".join([last_step + "-result", "json"])
    report_path = os.path.join(report_path_dir, report_json_file)

    step_info = read_report(report_path)
    _get_post_condition_info(step_info, {"after": finish_condition})
    write_report(report_path, step_info)
