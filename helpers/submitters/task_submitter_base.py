import builtins
import sys
from io import StringIO
from types import TracebackType
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from helpers.submitters.submitter import Submitter


class TaskSubmitterBase(Submitter):
    def __enter__(self) -> "TaskSubmitterBase":
        self._captured_output = StringIO()

        self._original_input = builtins.input
        self._original_stdout = sys.stdout

        builtins.input = self._simulate_input
        sys.stdout = self._captured_output

        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        builtins.input = self._original_input
        sys.stdout = self._original_stdout

    def _get_output(self) -> str:
        output = self._captured_output.getvalue()
        self._captured_output.truncate(0)
        self._captured_output.seek(0)
        return output

    def _set_input(self, values: List[str]) -> None:
        self._input_values = iter(values)

    def _show_results(self, test_results: List[bool]) -> None:
        if all(test_results):
            self._show_message("You have passed the tests! :)", "green")
        else:
            self._show_message(f"Tests passed: {test_results.count(True)}", "green")
            self._show_message(f"Tests failed: {test_results.count(False)}", "red")

    def _simulate_input(self, prompt: Any = None) -> str:
        if prompt:
            print(prompt)
        return str(next(self._input_values))

    def _test_return(
        self,
        func: Callable,
        data: List[
            Tuple[
                List[Union[int, float, str]],
                Union[int, float, str, List, Dict, Tuple, BaseException],
            ]
        ],
    ) -> None:
        test_results = []
        for input, output in data:
            if isinstance(output, BaseException):
                exc_type, exc_message = type(output), str(output)
                try:
                    test_results.append(func(*input) == output)
                except exc_type as ex:
                    test_results.append(str(ex) == exc_message)
            else:
                test_results.append(func(*input) == output)
        self._show_results(test_results)

    def _test_print(self, func: Callable, data: List[Tuple[List[str], str]]) -> None:
        test_results = []
        for input, output in data:
            self._set_input(input)
            func()
            test_results.append(self._get_output() == output)
        self._show_results(test_results)
