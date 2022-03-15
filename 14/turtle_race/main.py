import turtle as t
from random import randint
import turtle_class
import threading


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


screen = t.Screen()  # 0, 1000
turtles = []
t.colormode(255)
for i in range(5):
    turtle = t.Turtle()
    turtle.speed("fastest")
    turtle.color(random_color())
    turtle.penup()
    turtle.shape("turtle")
    turtle.setx(-400)
    turtle.sety(100 - i * 50)
    turtle.pendown()
    turtle.speed(1)
    turtle_full = turtle_class.Turtle(turtle, randint(45, 55))
    turtles.append(turtle_full)


def thread_func(given_turtle: turtle_class.Turtle):
    finnish_is_reached = False
    while not finnish_is_reached:
        pos = given_turtle.turtle.pos()
        given_turtle.turtle.setx(pos[0] + given_turtle.speed / 10)
        if given_turtle.turtle.pos()[0] >= 400:
            finnish_is_reached = True


# finnish_is_reached = False
# while not finnish_is_reached:
#     for a_turtle in turtles:
#         pos = a_turtle.turtle.pos()
#         a_turtle.turtle.setx(pos[0] + a_turtle.speed / 10)
#         if a_turtle.turtle.pos()[0] >= 400:
#             finnish_is_reached = True
threads = []
for a_turtle in range(len(turtles)):
    argument = turtles[a_turtle],
    t = threading.Thread(target=thread_func, args=argument)
    t.start()
    threads.append(t)
threading.main_thread().join()
for item in threads:
    item.join()

screen.exitonclick()
