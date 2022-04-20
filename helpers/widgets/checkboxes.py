from typing import List

from IPython.display import HTML, display
from ipywidgets import Checkbox, Layout, VBox


class MyCheckBoxes:
    def __init__(self, num_options: int) -> None:
        layout = Layout(margin="-5px 0 0 20px")
        self._checkboxes = [
            Checkbox(description=str(option_number + 1), indent=False, layout=layout)
            for option_number in range(num_options)
        ]

    def is_answer_correct(self, answer: List[int]) -> bool:
        return self._get_selected() == answer

    def show(self) -> None:
        display(HTML('<p style="margin-left: 5px">Choose the answer:</p>'))
        display(VBox(self._checkboxes))  # type: ignore

    def _get_selected(self) -> List[int]:
        return [
            (option_number + 1)
            for option_number in range(len(self._checkboxes))
            if self._checkboxes[option_number].value
        ]
