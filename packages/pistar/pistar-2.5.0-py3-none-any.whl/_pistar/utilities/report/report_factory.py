from typing import Dict
from _pistar.pistar_pytest.utils import now
from _pistar.utilities.constants.testcase import PISTAR_TESTCASE_EXECUTION_STATUS as \
    PISTAR_STATUS
from _pistar.utilities.testcase.case import TestCase
from _pistar.agent import generate_finish_file


def generate_status_and_finish_file(case: TestCase) -> Dict[str, int]:
    try:
        status = PISTAR_STATUS.PASSED if case.execution_status == "0" else PISTAR_STATUS.FAILED
        start_time = case.start_time
        if case.is_timeout:
            end_time = now()
            exception_info = "TimeoutError"
        else:
            end_time = case.end_time
            exception_info = None if status == PISTAR_STATUS.PASSED else \
                str(case.execution_exceptions[-1])
    except BaseException:
        status = PISTAR_STATUS.ERROR
        start_time = now()
        end_time = start_time
        exception_info = case.exception["detail"]
    generate_finish_file(
        output_dir=str(case.clazz.testcase_result_path),
        start_time=start_time,
        end_time=end_time,
        status=status,
        attach_path=str(case.clazz.logger_path),
        exception_info=exception_info
    )
    return {"::".join([case.path, case.name]): status}
