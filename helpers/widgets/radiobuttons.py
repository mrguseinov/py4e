from IPython.display import HTML, display
from ipywidgets import Layout, RadioButtons


class MyRadioButtons:
    def __init__(self, num_options: int) -> None:
        options = [str(option_number + 1) for option_number in range(num_options)]
        layout = Layout(margin="0 0 0 20px")
        self._radiobuttons = RadioButtons(options=options, layout=layout, value=None)

    def is_answer_correct(self, answer: int) -> bool:
        return self._get_selected() == answer

    def show(self) -> None:
        display(HTML('<p style="margin-left: 5px">Choose the answer:</p>'))
        display(self._radiobuttons)

    def _get_selected(self) -> int:
        selected = self._radiobuttons.value
        return 0 if selected is None else int(selected)
