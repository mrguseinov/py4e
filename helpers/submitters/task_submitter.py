from typing import Callable, Literal

from helpers.submitters.data import TASK_DATA
from helpers.submitters.task_submitter_base import TaskSubmitterBase


class TaskSubmitter(TaskSubmitterBase):
    def __init__(self, task_id: str, test_type: Literal["print", "return"]) -> None:
        self._task_data = TASK_DATA[task_id]
        self._test_type = test_type

    def submit(self, func: Callable) -> None:
        if self._test_type == "print":
            self._test_print(func, self._task_data)
        elif self._test_type == "return":
            self._test_return(func, self._task_data)
        else:
            raise ValueError("Wrong test type. Use 'print' or 'return'.")
