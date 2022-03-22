import turtle as t
import random


LEVEL = 1
screen = t.Screen()
screen.setup(500, 500)

player_turtle = t.Turtle()
player_turtle.shape("turtle")
player_turtle.speed(10)
player_turtle.setheading(90)
player_turtle.penup()
player_turtle.sety(-200)
state = "word"
loose_space = []


def move_forward():
    player_turtle.forward(20)


def move_backward():
    player_turtle.backward(20)


def move_left():
    player_turtle.setx(player_turtle.pos()[0] - 20)


def move_right():
    player_turtle.setx(player_turtle.pos()[0] + 20)


def fraction():
    print("ok")
    if player_turtle.pos()[1] == 200 or player_turtle.pos()[1] > 200:
        return

    screen.ontimer(fraction, 100)


def update_obstacles():
    count_of_objects = random.randint(-10, 3)
    if count_of_objects > 0:
        for i in range(count_of_objects):
            continue



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.ontimer(fraction, 2000)
fraction()
screen.mainloop()
# game_running = True
# while game_running:
#     if state == "finished":
#         game_running = True
#     screen.onkey(move_forward, "w")
#     screen.onkey(move_backward, "s")
#     screen.onkey(move_right, "d")
#     screen.onkey(move_left, "a")

screen.exitonclick()
