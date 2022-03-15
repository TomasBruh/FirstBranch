import turtle as t
from random import randint

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")

screen = t.Screen()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_square(size):
    for _ in range(4):
        tim.forward(size)
        tim.left(90)
        tim.color(random_color())


def draw_dash(dash_size, dashes):
    for _ in range(dashes):
        tim.forward(dash_size)
        tim.penup()
        tim.forward(dash_size)
        tim.pendown()
        tim.color(random_color())


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)
        tim.color(random_color())


def draw_spirograph(radius, size_of_gap):
    tim.speed("fastest")
    for angle in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


def move_forward():
    tim.forward(10)
    tim.color(random_color())


def move_backward():
    tim.backward(10)
    tim.color(random_color())


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.color(random_color())


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.color(random_color())


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")

# tim.color(random_color())
# draw_square(100)
# tim.right(90)
# draw_dash(5, 15)
# draw_shape(6)
# draw_spirograph(100, 1)






screen.exitonclick()

