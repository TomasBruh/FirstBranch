from question import Question


class QuestionBank:
    def __init__(self, questions: list):
        self.questions = questions

    def print_question(self, index: int):  # or remove question
        """ Print needed question """
        self.questions[index].question = self.questions[index].question[0].upper() + self.questions[index].question[1:]
        print(self.questions[index].question)

    def answer_is_correct(self, index: int, answer: str):
        """ Returns true if the answer is correct an false if it is not. If the given answer
        does not mach the answers stored in the object, user will be asked to input a new answer. """
        if self.questions[index].correct_answer.lower() == answer.lower():
            return True
        for incorrect_answer in self.questions[index].incorrect_answers:
            if incorrect_answer.lower() == answer.lower():
                return False
        answers = [self.questions[index].correct_answer] + self.questions[index].incorrect_answers
        answers.sort()
        print(f"The answer is invalid. You must choose between: {answers}")
        new_answer = input("Try again: ")
        return self.answer_is_correct(index, new_answer)
