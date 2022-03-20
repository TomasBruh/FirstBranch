from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race. Enter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

stats = {}
with open("stats.txt", 'r') as read_stream:
    data = read_stream.read().split("|")
    read_stream.close()

for item in data:
    item_info = item.split(" ")
    stats[item_info[0]] = item_info[1]
stats[winning_color] = int(stats[winning_color]) + 1
stats["games"] = int(stats["games"]) + 1
with open("stats.txt", "w") as write_stream:
    write_string = ""
    for key, value in stats.items():
        write_string += f"{key} {value}|"
    write_string = write_string[:-1]
    write_stream.write(write_string)
    write_stream.close()


def print_statistics(statistics: dict):
    statistics2 = statistics
    del statistics2["games"]
    for a_key, a_value in statistics.items():
        print(f"{a_key} color has won {a_value} times out of {statistics2['games']} games")


print_statistics(stats)
screen.exitonclick()
