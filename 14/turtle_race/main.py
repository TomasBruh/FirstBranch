import turtle as t
from random import randint
import turtle_class


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


t.colormode(255)
screen = t.Screen()  # 0, 1000
screen.screensize(2000, 1500)
screen.delay(5)


def generate_turtles(amount):
    turtles_ = []
    for i in range(amount):
        turtle = t.Turtle()
        turtle.speed(5)
        turtle.color(random_color())
        turtle.penup()
        turtle.shapesize(1.5, 1.5, 2)
        turtle.shape("turtle")
        turtle.setx(75 - screen.window_width() / 2)
        turtle.sety(100 - i * 50)
        turtle_full = turtle_class.Turtle(turtle, randint(20, 40))
        turtles_.append(turtle_full)
    return turtles_


turtles = generate_turtles(5)
guess = int(t.numinput("Guess which turtle is going to win!", ""))
finnish_is_reached = False
winner = 0
while not finnish_is_reached:
    winner = 0
    for a_turtle in turtles:
        winner = winner + 1
        pos = a_turtle.turtle.pos()
        a_turtle.turtle.setx(pos[0] + a_turtle.speed)
        print(winner)
        if a_turtle.turtle.pos()[0] >= screen.window_width() / 2 - 75:
            finnish_is_reached = True

            if turtles[guess - 1] == a_turtle:
                print("Congrats, your guess was correct! Your turtle has won!")
            else:
                print("You turtle has lost.")
            break
        t.update()
stats_of_turtles = []
with open("stats.txt", "r") as read_stream:
    data = read_stream.readlines()
    read_stream.close()
for item in stats_of_turtles:
    print(item)
print("lol" + str(len(stats_of_turtles)))
stats_of_turtles[winner - 1] = str(int(stats_of_turtles[winner - 1]) + 1)
with open("stats.txt", "w") as write_stream:
    write_stream.writelines(stats_of_turtles)
screen.exitonclick()
