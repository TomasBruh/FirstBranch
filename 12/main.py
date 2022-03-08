import question_data
from question import Question
from question_bank import QuestionBank
questions = list()
for question in question_data.question_data:

    questions.append(Question(question["category"], question["type"], question["difficulty"], question["question"],
                              question["correct_answer"], question["incorrect_answers"]))
question_bank = QuestionBank(questions)
# for i in range(len(question_bank)):
#     print(question_bank[i])
print(question_bank.answer_is_correct(0, "True"))
