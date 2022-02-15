
def choose_difficulty():
    """ Returns a wanted difficulty """

    class Difficulty:
        def __init__(self, name, lives, hints, answer_range):
            self.lives = lives
            self.hints = hints
            self.name = name
            self.range = answer_range

    difficulties = [
        Difficulty("Easy", 9, True, 50),
        Difficulty("Normal", 6, True, 100),
        Difficulty("Hard", 3, False, 30)
    ]
    difficulty_string = ""
    for difficulty in difficulties:
        difficulty_string += "/" + difficulty.name
    difficulty_string = difficulty_string[1:]

    def find_difficulty():
        while True:
            inserted_difficulty = input(f"Which level of difficulty would you like? ({difficulty_string}) - ")
            for item in difficulties:
                if item.name.lower() == inserted_difficulty.lower():
                    difficulty_find = item
                    return difficulty_find
            print(f"There is no difficulty with the name '{inserted_difficulty}', try again.")

    return find_difficulty()
