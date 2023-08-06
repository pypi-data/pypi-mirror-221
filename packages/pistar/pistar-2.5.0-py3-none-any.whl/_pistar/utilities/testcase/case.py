# -*- coding: utf-8 -*-
"""
description: this module provides class BaseTestCase.
"""
import collections
import inspect
import os
import queue
import shutil
import threading
import functools
from pathlib import Path
from typing import Callable
from typing import Dict
from typing import Optional
from typing import TYPE_CHECKING
from typing import Type
from typing import TypeVar
from typing import Union
from attr import Factory
from attr import attrib
from attr import attrs

from _pistar.caller import ExecuteInfo
from _pistar.config import Config
from _pistar.node import Node
from _pistar.pistar_pytest.utils import now
from _pistar.pistar_pytest.utils import sha256_slice
from _pistar.utilities.assertion.assert_that import AssertThat
from _pistar.utilities.condition.condition import ConditionLookUpError
from _pistar.utilities.condition.condition import ConditionManager
from _pistar.utilities.constants.testcase import ControlArgs
from _pistar.utilities.constants.testcase import TESTCASE_EXECUTION_STATUS as STATUS
from _pistar.utilities.exceptions.testcase import BlockedException
from _pistar.utilities.exceptions.testcase import FailedException
from _pistar.utilities.exceptions.testcase import InvestigatedException
from _pistar.utilities.exceptions.testcase import PassedException
from _pistar.utilities.exceptions.testcase import TestCaseStatusException
from _pistar.utilities.exceptions.testcase import UnavailableException
from _pistar.utilities.exceptions.testcase import UnexecutedException
from _pistar.utilities.exceptions.testcase import ControlArgumentTypeException
from _pistar.utilities.exceptions.testcase import ControlUsageException
from _pistar.utilities.logger.logger import Logger
from _pistar.utilities.logger.logger import ExecuteLogger
from _pistar.utilities.testcase.assert_that import assert_that as _assert_that
from _pistar.utilities.testcase.exception import ExcInfoFormatter
from _pistar.utilities.testcase.exception import ExceptionInfo
from _pistar.utilities.testcase.steps import has_teststep, Step
from _pistar.utilities.testcase.steps import ParametersLookUpError
from _pistar.utilities.testcase.steps import is_teststep
from _pistar.utilities.testcase.steps import TimeoutLookUpError
from _pistar.utilities.parameters.parameters import ParametersLinkLookupError
from _pistar.utilities.constants.pistar_logging import LOGGING_LEVEL


if TYPE_CHECKING:
    from _pistar.main import Session

BASE_TEST_CASE = "BaseTestCase"


def get_parent_case_from_call_stack():
    """
    description: this function is used to get the parent testcase from the call stack.
    """
    caller_frame = inspect.currentframe()
    while True:
        if 'self' in caller_frame.f_locals:
            testcase = caller_frame.f_locals['self']
            if isinstance(testcase, BaseTestCase):
                return testcase
        caller_frame = caller_frame.f_back
        if caller_frame is None:
            return None


class MetaTestCase(type):
    """
    description: this class is the meta class of BastTestCase.
    """

    def __init__(cls, *args, **kwargs):
        """
        description: this function is used to execute testcase automatically
        """
        super().__init__(*args, **kwargs)

        return

    def __new__(mcs, name, bases, class_dict):
        bases = (object,) if name == BASE_TEST_CASE else bases

        new_class = type.__new__(mcs, name, bases, class_dict)

        return new_class

    def __call__(cls, *args, **kwargs):
        """
        description: this function is used for testcase introspection.
        """
        parent = get_parent_case_from_call_stack()
        if parent:
            cls._no_color = parent._no_color
            cls._log_level = parent._log_level
            cls.logger_path = parent.logger_path
            cls.__initialize__()

        testcase = type.__call__(cls, *args, **kwargs)


        if not testcase.failure:
            def failure():
                return testcase.teardown()

            testcase.failure = failure

        return testcase


class TeststepQueue(set):
    """
    this class is used to save the teststeps and pop avaliable teststeps.
    """

    def pop_teststeps(self):
        """
        description: this member functions is uses to
                     pop the avaliable teststeps.
        """
        teststeps = {teststep for teststep in self if teststep.start()}
        self.difference_update(teststeps)
        return teststeps


class BaseTestCase(metaclass=MetaTestCase):
    """
    this class is the base class of testcase.
    """

    __execution_status = None
    __start_time = None
    __end_time = None
    __assertion_list = None
    __action_word_information = None
    __status_dictionary = None
    __globals = None
    logger_path = None
    __report_path = None
    _no_color = None
    _log_level = None
    testcase_result_path = None
    failure = None
    timeout: int = 0

    user_logger = None
    debug: Callable[[str], None] = None
    info: Callable[[str], None] = None
    warning: Callable[[str], None] = None
    error: Callable[[str], None] = None
    critical: Callable[[str], None] = None

    @classmethod
    def __initialize__(cls):
        """
        description: this is the constructor of the class BaseTestCase.
        """
        # initialize the logger
        cls.__assertion_list = list()
        cls.__action_word_information = collections.defaultdict(list)

        cls.__status_dictionary = {
            STATUS.PASSED: PassedException,
            STATUS.FAILED: FailedException,
            STATUS.BLOCKED: BlockedException,
            STATUS.INVESTIGATED: InvestigatedException,
            STATUS.UNAVAILABLE: UnavailableException,
            STATUS.UNEXECUTED: UnexecutedException,
        }

        cls.user_logger = Logger(
            name=cls.__name__,
            logger_format="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(funcName)s]\n%(message)s",
            output_path=cls.logger_path,
            level=getattr(LOGGING_LEVEL, cls._log_level.upper()),
            no_color=cls._no_color,
        )

        cls.debug: Callable[[str], None] = cls.user_logger.debug
        cls.info: Callable[[str], None] = cls.user_logger.info
        cls.warning: Callable[[str], None] = cls.user_logger.warning
        cls.error: Callable[[str], None] = cls.user_logger.error
        cls.critical: Callable[[str], None] = cls.user_logger.critical

    @property
    def status(self):
        """
        description: user can fetch testcase status with this attribute.
        """
        return self.__execution_status

    @status.setter
    def status(self, value):
        """
        description: if user set this attribute, raise corresponding exception.
        """
        frame = inspect.currentframe()
        line_number = frame.f_back.f_lineno
        raise self.__status_dictionary[value](line_number)

    def setup(self):
        """
        description: this is the setup of testcase.
        """
        return

    def teardown(self):
        """
        description: this is the teardown of testcase.
        """
        return

    def assert_that(self, value) -> AssertThat:
        """
        description: this member function is used to make assertion.
        arguments:
            value:
                type: any
                description: the value to be asserted
        return:
            type: assert_that
            description: if assertion is passed, return itself,
                         if it is failed, raise exception
        """
        return _assert_that(value=value, testcase=self)

    def append_action_word_execution_information(
        self, module_name, caller_name, action_word_name, time_consuming
    ):
        """
        description: this function is used to add action word information into
                     member variable __action_word_information.
        arguments:
            module_name:
                type: str
                description: the module name of the action word
            action_word_name:
                type: str
                description: the name of the action word
            time_consuming:
                type: float
                description: the time consuming of action word execution,
                             unit is second
        """
        self.__action_word_information[
            ".".join([module_name, caller_name, action_word_name])
        ].append(time_consuming)

    @property
    def execution_status(self):
        """
        description: return the execution status of this testcase.
        """
        return self.__execution_status

    @property
    def action_word_information(self):
        """
        description: return the action word information of this testcase.
        """
        return self.__action_word_information

    @classmethod
    def __parse_arguments__(cls, output, no_color=False, log_level="info"):
        """
        description: this function is used to parse the command from console.
        todo:move this function out of the case class.
        """
        cls._no_color = no_color
        cls._log_level = log_level
        output_abspath = os.path.abspath(output)
        if not os.path.exists(output_abspath):
            os.makedirs(output_abspath)
        case_sha256_name = sha256_slice(inspect.getfile(cls))
        cls.testcase_result_path = os.path.join(
            output_abspath, case_sha256_name
        )
        if os.path.exists(cls.testcase_result_path):
            shutil.rmtree(cls.testcase_result_path)
        os.makedirs(cls.testcase_result_path)
        report_path = os.path.join(cls.testcase_result_path, case_sha256_name + ".html")
        logger_path = os.path.join(
            cls.testcase_result_path, case_sha256_name + "-attachment.log"
        )
        cls.logger_path = logger_path
        cls.__report_path = report_path


def get_result_path(output_path, rel_path):
    result_path = output_path.joinpath(sha256_slice(str(rel_path.absolute())))
    result_path.mkdir(parents=True, exist_ok=True)
    return result_path


@attrs
class TestCaseStepRecord:
    condition_result_cache = attrib(type=dict, default=Factory(dict))
    start_time = attrib(type=int, default=None)
    end_time = attrib(type=int, default=None)
    status_code = attrib(type=str, default=None)
    exception = attrib(type=dict, default=Factory(dict))


T = TypeVar("T", bound=BaseTestCase)


class TestCaseController:
    """
    description: the control decorator implementation
    """

    def __init__(self, rigorous=None, timeout: float = 0):
        self.rigorous = rigorous
        self.timeout = timeout

    def __call__(self, cls: Type[T], *args, **kwargs):
        self.__type_check(cls)
        cls._rigorous = self.rigorous
        cls.timeout = self.timeout
        return cls

    def __type_check(self, cls: Type[T]):
        """
        description: check the validity of the control decorator
        """
        # the control decorator should only be used for test cases
        try:
            is_case = issubclass(cls, BaseTestCase)
        except TypeError as e:
            raise ControlUsageException from e
        else:
            if is_case is not True:
                raise ControlUsageException

        # the control decorator argument 'rigorous' should be of Boolean type
        if self.rigorous is not None and not isinstance(self.rigorous, bool):
            raise ControlArgumentTypeException("rigorous", self.rigorous, bool)
        if not isinstance(self.timeout, (int, float)) or self.timeout < 0:
            raise TypeError("timeout must be a positive integer")


def control(cls: Union[Type[T], None] = None, *, rigorous: bool = None, timeout: float = 0):
    """
    description: the control decorator used to decorate test case
    """
    controller = TestCaseController(rigorous=rigorous, timeout=timeout)

    # when the control decorator has no arguments, cls is the class which be
    # wrapped, otherwise cls is None
    if cls:
        return controller(cls=cls)

    return controller


class TestCase(Node):
    """A Class responsible for setting up and executing a pistar test case.

    param case_obj:
        The origin pistar test case derived from BaseTestCase.
    param arguments:
        The console parameter.
    """

    _start_time = None
    _end_time = None
    __execution_status = None

    execute_records = dict()

    def __init__(
        self,
        name: str,
        fspath: Optional[Path] = None,
        obj=None,
        parent: Optional["Node"] = None,
        config: Optional["Config"] = None,
        session: Optional["Session"] = None,
    ) -> None:
        super().__init__(
            name=name,
            fspath=fspath,
            parent=parent,
            config=config,
            session=session,
        )

        self._obj = obj

        self.execute_records = dict()
        self.exception = dict()
        self.execution_exceptions = list()
        self.reports = list()
        self.__exception_instance_queue = queue.Queue()

        self.instance = None
        self.setup = None
        self.teardown = None
        self.failure = None
        self.is_timeout = False
        self.timeout = 0
        self.hook = self.config.hook
        if self.session.config.debug:
            self.__logger_path = os.path.join(os.getcwd(), "logs", "pistar.log")
            self.logger = ExecuteLogger(
                name=name,
                logger_format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
                output_path=self.__logger_path,
            )

    @classmethod
    def from_parent(cls, parent: "Node", *, name, obj, **kwargs):
        return super().from_parent(parent=parent, name=name, obj=obj, **kwargs)

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def clazz(self) -> Type[BaseTestCase]:
        return self._obj

    @property
    def execution_status(self):
        return self.__execution_status

    @execution_status.setter
    def execution_status(self, value):
        self.__execution_status = value

    @property
    def path(self) -> str:
        """case file absolute path."""
        return str(self.fspath)

    @property
    def condition_manager(self) -> ConditionManager:
        return self.session.condition_manager

    def debug(self, message):
        if getattr(self, "logger", None):
            self.logger.debug(message)

    def info(self, message):
        if getattr(self, "logger", None):
            self.logger.info(message)

    def warning(self, message):
        if getattr(self, "logger", None):
            self.logger.warning(message)

    def error(self, message):
        if getattr(self, "logger", None):
            self.logger.error(message)

    def critical(self, message):
        if getattr(self, "logger", None):
            self.logger.critical(message)

    def initialize_step(self):
        self._obj.__parse_arguments__(
            self.session.config.outpath, self.session.config.no_color,
            self.session.config.log_level
        )
        self._obj.__initialize__()
        self.instance = self._obj()
        self.setup = self.instance.setup
        self.teardown = self.instance.teardown
        self.failure = self.instance.failure

        self.__schedule_step()

    @staticmethod
    def format_exception_by_pure_traceback(dependence: Callable) -> Dict[str, str]:
        """
        description: Format the complete exception information to get the
        pure exception information on the script side
        """
        exc_info = ExceptionInfo.from_current()
        fmt = ExcInfoFormatter(exc_info=exc_info, func=dependence)

        exception_title = exc_info.exc_only()
        if isinstance(exc_info.value, (ConditionLookUpError, ParametersLookUpError,
                                       TimeoutLookUpError, ParametersLinkLookupError)):
            exc_repr = exc_info.value.format_repr()
        else:
            exc_repr = fmt.repr_impl_exception()
        exception = dict()
        if isinstance(exc_repr, list):
            exception_detail = "\n".join([str(per_exc_repr) for per_exc_repr in exc_repr])
            exception["lineno"] = exc_repr[-1].location.lineno
        else:
            exception_detail = str(exc_repr)
            exception["lineno"] = exc_repr.location.lineno
        exception["title"] = exception_title
        exception["detail"] = exception_detail
        return exception

    def __set_manual_status(self, exception):
        """
        description: when the result is manually specified by self.status
        in the test case script, the test case result is set according to the
        corresponding exception class

        :param exception: exception class corresponding to manual status
        :type exception: TestCaseStatusException
        """
        if isinstance(exception, PassedException):
            self.__execution_status = STATUS.PASSED
            self.instance.info(exception)
        elif isinstance(exception, FailedException):
            self.__execution_status = STATUS.FAILED
            self.instance.error(exception)
        elif isinstance(exception, InvestigatedException):
            self.__execution_status = STATUS.INVESTIGATED
            self.instance.error(exception)
        elif isinstance(exception, UnavailableException):
            self.__execution_status = STATUS.UNAVAILABLE
            self.instance.error(exception)
        elif isinstance(exception, BlockedException):
            self.__execution_status = STATUS.BLOCKED
            self.instance.error(exception)
        elif isinstance(exception, UnexecutedException):
            self.__execution_status = STATUS.UNEXECUTED
            self.instance.error(exception)

    def __schedule_step(self):
        teststep_queue = list()

        child = self.instance.__class__
        for attribute_name in child.__dict__:
            if is_teststep(child.__dict__.get(attribute_name)):
                teststep_queue.append(getattr(self.instance, attribute_name))

        self.teststep_queue = TeststepQueue(teststep_queue)

    def __run(
        self, dependence: Callable
    ) -> Union[TestCaseStatusException, BaseException, None]:
        step = Step.from_case_and_teststep(case=self, step=dependence)
        step.setup()
        if step.name == "setup":
            when = "setup"
        else:
            when = "teardown"
        call_info = ExecuteInfo.from_call(call=step.execute, when=when)
        report = self.hook.pistar_make_report(case=self, step=step, call_info=call_info)
        return report.exception

    def teststep_thread(self, step: Step):
        call_info = ExecuteInfo.from_call(step.execute, when="call")
        report = self.hook.pistar_make_report(case=self, step=step,
                                              call_info=call_info)
        self.reports.append(report)
        self.__exception_instance_queue.put(report.exception)

    def _set_test_step_status(self, test_step):
        # when test case configured by '@control(rigorous=False)',let test step be
        # marked as 'end' even if it has exceptions
        if getattr(self.instance, ControlArgs.RIGOROUS, None) is False:
            test_step.end.value = True

    def _set_execute_records(self, step: Callable, tc_step_record: TestCaseStepRecord):
        """
        description: Set the execution result for each step
        :param step: setup,teardown,failure or test step
        :type step: Callable
        :param tc_step_record: record for one step
        :type tc_step_record: TestCaseStepRecord
        :return: None
        """
        self.execute_records[step.__name__] = {
            "before": tc_step_record.condition_result_cache,
            "start_time": tc_step_record.start_time,
            "end_time": tc_step_record.end_time,
            "status_code": tc_step_record.status_code,
            "exception": tc_step_record.exception,
        }

    def execute(self):
        self._start_time = now()
        self.__execution_status = STATUS.PASSED

        exception_inst = self.__run(self.setup)
        if isinstance(exception_inst, PassedException):
            self.__run(self.teardown)
        elif exception_inst:
            self.__run(self.failure)
        else:
            exception_inst = self._loop()
            if exception_inst and not isinstance(exception_inst, PassedException):
                self.__execution_status = STATUS.FAILED
                self.__run(self.failure)
            else:
                self.__execution_status = STATUS.PASSED
                self.__run(self.teardown)
        self._end_time = now()

    def _loop(self):
        threads = list()
        ts_last_exception = None
        while self.teststep_queue:
            teststeps = self.teststep_queue.pop_teststeps()
            for teststep in teststeps:
                step = Step.from_case_and_teststep(case=self, step=teststep)
                step.setup()
                thread = threading.Thread(
                    target=functools.partial(self.teststep_thread, step)
                )
                threads.append(thread)
                thread.start()

            exception_inst = self.__exception_instance_queue.get()
            if exception_inst:
                ts_last_exception = exception_inst
            # TestCaseStatusException priority is greater than @control
            control_status = getattr(self.instance, ControlArgs.RIGOROUS, None)
            if (exception_inst and control_status is not False) or (
                isinstance(exception_inst, TestCaseStatusException)
                and control_status is False
            ):
                break
        return ts_last_exception


def is_test_case(obj) -> bool:
    """Return True is the object is a Pistar TestCase and has test_step function."""
    return inspect.isclass(obj) and issubclass(obj, BaseTestCase) and has_teststep(obj)


def get_testcase_from_module(module, abs_path) -> Optional[BaseTestCase]:
    """
    description: the function is used to get the testcase class in the module
    """
    for item in dir(module):
        if item.startswith("_"):
            continue
        obj = getattr(module, item, None)
        if is_test_case(obj) and inspect.getfile(obj) == abs_path:
            return obj
    return None
