import random
from difficulty import choose_difficulty

print("---Guess the number---")
program_is_running = True
while program_is_running:
    chosen_difficulty = choose_difficulty()
    print(f"The answer is between 1 and {chosen_difficulty.range}")
    the_answer = random.randint(1, chosen_difficulty.range)
    print(the_answer)
    game_is_running = True
    lives_left = chosen_difficulty.lives
    while game_is_running:
        guess_not_int = True
        guess = 0
        while guess_not_int:
            try:
                guess = int(input("Your guess - "))
                guess_not_int = False
            except ValueError:
                print("You have to input a number, retry.")
        if not guess == the_answer:
            print("That is not the answer.")
            lives_left -= 1
            print(f"You have {lives_left} lives left.")
            if lives_left == 0:
                print("Damn, you lost because you have no more lives left.")
                print(f"The answer was {the_answer}")
                game_is_running = False
            elif chosen_difficulty.hints:
                if the_answer > guess:
                    print("The answer is a bigger number.")
                else:
                    print("The answer is a smaller number.")
        else:
            print(f"Well done! You are correct, {guess} is the answer.")
            game_is_running = False

    if input("Would you like to play again? (Yes/No) -  ").lower() == "no":
        program_is_running = False
