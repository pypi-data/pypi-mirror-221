from typing import TYPE_CHECKING, Optional

from pluggy import HookspecMarker



if TYPE_CHECKING:
    from _pistar.config import Config
    from _pistar.main import Session
    from _pistar.caller import ExecuteInfo
    from _pistar.utilities.testcase.case import TestCase
    from _pistar.utilities.condition.condition import ConditionDef
    from _pistar.utilities.testcase.steps import Step
    from _pistar.result import Result

hookspec = HookspecMarker("pistar")


@hookspec
def pistar_add_option(config: "Config") -> None:
    """
    the function is used to register the command and arguments
    """
    ...


@hookspec
def pistar_config(config: "Config"):
    """
    the function is used to get the pluginmanager from config, and register the plugin's hook.
    """
    ...


@hookspec(firstresult=True)
def pistar_main(config: "Config"):
    """
    the function is the entry of the execution.
    """
    ...


@hookspec
def pistar_collection(session: "Session"):
    """
    the function is used to collect the testcases, conditions.
    """
    ...


@hookspec
def pistar_modify_case(case: "TestCase"):
    ...


@hookspec
def pistar_collect_finish(session: "Session"):
    """
    the function is used to collect the testcases, conditions.
    """
    ...


@hookspec(firstresult=True)
def pistar_run_loop(session: "Session"):
    """
    the function is the entry of executing the cases
    """
    ...


@hookspec
def pistar_run_procedure(case: "TestCase", next_case: Optional["TestCase"]):
    ...


@hookspec
def pistar_run_log_begin(case: "TestCase"):
    ...


@hookspec
def pistar_run_log_end(case: "TestCase"):
    ...


@hookspec
def pistar_session_start(session: "Session"):
    ...


@hookspec
def pistar_session_finish(session: "Session"):
    ...


@hookspec
def pistar_case_init(case: "TestCase"):
    ...


@hookspec(firstresult=True)
def pistar_condition_setup(condition_def: "ConditionDef", caller: "Step"):
    ...


@hookspec(firstresult=True)
def pistar_step_call(step: "Step"):
    ...


@hookspec(firstresult=True)
def pistar_make_init_report(case: "TestCase", call_info: "ExecuteInfo") -> "Result":
    ...


@hookspec(firstresult=True)
def pistar_make_report(case: "TestCase", step: "Step", call_info: "ExecuteInfo") -> \
        "Result":
    ...
