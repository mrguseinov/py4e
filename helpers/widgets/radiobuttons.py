from IPython.display import HTML, display
from ipywidgets import Layout, RadioButtons


class MyRadioButtons:
    def __init__(self, num_options: int) -> None:
        options = range(1, num_options + 1)
        layout = Layout(margin="0 0 0 20px")
        self._radiobuttons = RadioButtons(options=options, layout=layout, value=None)

    def is_answer_correct(self, answer: int) -> bool:
        return self._get_selected() == answer

    def show(self) -> None:
        display(HTML('<p style="margin-left: 5px">Choose the answer:</p>'))
        display(self._radiobuttons)

    def _get_selected(self) -> int:
        return self._radiobuttons.value or 0  # type: ignore
