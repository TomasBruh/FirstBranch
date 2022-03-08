class Question:
    def __init__(self, category: str, type_: str, difficulty: str, question: str, correct_answer: str,
                 incorrect_answers: list):
        self.category = category,
        self.type_ = type_,
        self.difficulty = difficulty,
        self.question = question,
        self.correct_answer = correct_answer,
        self.incorrect_answers = incorrect_answers
    # "category": "Science: Computers",
    # "type": "boolean",
    # "difficulty": "medium",
    # "question": "The HTML5 standard was published in 2014.",
    # "correct_answer": "True",
    # "incorrect_answers": [
    #     "False"
