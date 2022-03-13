from question_bank import QuestionBank


class QuizBrain:
    def __init__(self, question_bank: QuestionBank, high_score):
        self.question_bank = question_bank
        self.score = 0
        self.high_score = high_score

    def run_program(self):
        """ Initiates the program """
        print("----------------- Quiz -----------------")
        self.score = 0
        questions_count = len(self.question_bank.questions)
        print(f"There will be {questions_count} question(s) in this quiz.")
        for i in range(questions_count):
            self.question_bank.print_question(i)
            answer = input("Answer: ")
            if self.question_bank.answer_is_correct(i, answer) is True:
                self.score += 1
        print("The quiz has ended.")
        print(f"Your score: {self.score}")




