from typing import List, Union

from helpers.submitters.data import QUIZ_ANSWERS
from helpers.submitters.submitter import Submitter
from helpers.widgets import MyCheckBoxes, MyRadioButtons


class QuizSubmitter(Submitter):
    def __init__(self, quiz_id: str) -> None:
        self._quiz_answers = QUIZ_ANSWERS[quiz_id]

    def submit(
        self, questions: Union[List[MyCheckBoxes], List[MyRadioButtons]]
    ) -> None:
        for id, question in enumerate(questions):
            if question.is_answer_correct(self._quiz_answers[id]):
                self._show_message(f"Question {id}: Right.", "green")
            else:
                self._show_message(f"Question {id}: Wrong.", "red")
