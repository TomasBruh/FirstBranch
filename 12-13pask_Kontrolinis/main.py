import question_data
from question import Question
from question_bank import QuestionBank
import quiz_brain

def sort_by_difficulty(list_of_given_questions):
    """ Sorts a list of question objects into a list of question objects with the same difficulty,
    selected by the user """
    existing_difficulties = []
    for a_question in list_of_given_questions:
        existing_difficulties += [a_question.difficulty.lower()]
    existing_difficulties = list(set(existing_difficulties))
    difficulties = ""
    for difficulty in existing_difficulties:
        difficulties += "; " + difficulty
    difficulties = difficulties[2:]
    chosen_difficulty = input(f"What difficulty would you like? You can choose from:  {difficulties} - ").lower()
    while not existing_difficulties.__contains__(chosen_difficulty):
        print(f"There is no {chosen_difficulty} difficulty.")
        print(f"You must choose from the given difficulties: {difficulties}.")
        chosen_difficulty = input("Insert an existing difficulty: ").lower()
    difficult_questions = []
    for difficult_question in list_of_given_questions:
        if difficult_question.difficulty.lower() == chosen_difficulty.lower():
            difficult_questions += [difficult_question]
    return difficult_questions


def sort_by_category(list_of_given_questions):
    """ Sorts a list of question objects into a list of question objects with the same category,
        selected by the user """
    existing_categories = []
    for a_question in list_of_given_questions:
        existing_categories += [a_question.category.lower()]
    existing_categories = list(set(existing_categories))
    categories_string = ""
    for a_category in existing_categories:
        categories_string += "; " + a_category
    categories_string = categories_string[2:]
    chosen_category = input(f"What category would you like? You can choose from:  {categories_string} - ").lower()
    while not existing_categories.__contains__(chosen_category):
        print(f"There is no {chosen_category} category.")
        print(f"You must choose from the given categories:  {categories_string}.")
        chosen_category = input("Insert an existing category: ").lower()
    sorted_list = []
    for a_question in list_of_given_questions:
        if a_question.category.lower() == chosen_category.lower():
            sorted_list += [a_question]
    return sorted_list


def sort_boolean(given_list):
    """ Removes any non-boolean question objects out of a list """
    sorted_list = []
    for a_question in given_list:
        if a_question.type_ == "boolean":
            sorted_list.append(a_question)
    return sorted_list


all_questions = []
for question in question_data.question_data:
    all_questions.append(Question(question["category"], question["type"], str(question["difficulty"]),
                                  question["question"], question["correct_answer"], question["incorrect_answers"]))
print("---- Quiz setup ----")
sorted_questions = sort_boolean(all_questions)
difficulty_sorted_questions = sort_by_difficulty(all_questions)
difficulty_category_sorted_questions = sort_by_category(difficulty_sorted_questions)

question_bank = QuestionBank(difficulty_category_sorted_questions)
quiz_brain.run_game(question_bank)
