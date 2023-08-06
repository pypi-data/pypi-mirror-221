from typing import Callable
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union
from typing import cast
from typing import TYPE_CHECKING
import attr

from _pistar.node import Collector
from _pistar.pistar_pytest.utils import now

from _pistar.utilities.testcase.exception import ExceptionInfo

if TYPE_CHECKING:
    from _pistar.utilities.testcase.case import TestCase
    from typing_extensions import Literal

TResult = TypeVar("TResult", covariant=True)


@attr.s(init=False, auto_attribs=True)
class ExecuteInfo(Generic[TResult]):
    _result: Optional[TResult]
    # the exception of the call,if raised.
    exc_info: Optional[ExceptionInfo[BaseException]]
    # the time when the call started,in micro-seconds since the epoch.
    begin: int
    # the time when the call finished,in micro-seconds since the epoch.
    end: int

    # the time cost,in micro-seconds.
    duration: int

    def __init__(
        self,
        result: Optional[TResult],
        exc_info: Optional[ExceptionInfo[BaseException]],
        begin: int,
        end: int,
        duration: int,
        when: "Literal['collect', 'init', 'setup', 'call', 'teardown']"
    ) -> None:
        self._result = result
        self.exc_info = exc_info
        self.begin = begin
        self.end = end
        self.duration = duration
        self.when = when

    @property
    def result(self) -> TResult:
        """
        The return value of the call.

        Can accessed without exception raised.
        """
        if self.exc_info is not None:
            raise AttributeError("no valid result")
        return cast(TResult, self._result)

    @classmethod
    def from_call(
        cls,
        call: Callable[[], TResult],
        when: "Literal['collect', 'init', 'setup', 'call', 'teardown']"
    ) -> "ExecuteInfo[TResult]":
        exc = None
        begin = now()
        try:
            result: Optional[TResult] = call()
        except TimeoutError as e:
            raise e
        except BaseException:
            exc = ExceptionInfo.from_current()
            result = None


        end = now()

        duration = end - begin

        return cls(
            result=result,
            exc_info=exc,
            begin=begin,
            end=end,
            duration=duration,
            when=when
        )


class CollectReport:
    def __init__(
        self,
        status: str,
        errors: str,
        result: Optional[List[Union["TestCase", "Collector"]]],
    ) -> None:
        self.status = status
        self.errors = errors
        self.result = result

    @property
    def passed(self):
        return self.status == "passed"

    @property
    def failed(self):
        return self.status == "failed"
