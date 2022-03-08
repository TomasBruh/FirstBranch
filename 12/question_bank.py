from question import Question


class QuestionBank:
    def __init__(self, questions: list):
        self.questions = questions
        print(type(self.questions))
        print(type(questions))


        # for category, type_, difficulty, question, correct_answer, incorrect_answers in questions:
        #     self.questions.append(Question(category, type_, difficulty, question, correct_answer, incorrect_answers))

    def print_question(self, index: int):  # or remove question
        """ Print needed question """
        # self.questions[index] = self.questions[index].a
        print(self.questions[index].question)

    def answer_is_correct(self, index: int, answer: str):  # doesnt work
        if self.questions[index].correct_answer == answer:
            return True
        for incorrect_answer in self.questions[index].incorrect_answers:
            if incorrect_answer == answer:
                return False
        print(type(self.questions[index].type_))
        return False
