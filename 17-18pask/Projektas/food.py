import turtle
import random

generator_int = 1


class Food:
    def __init__(self, screen: turtle.Screen()):
        self.food_array = []
        self.screen = screen

    def generate_food(self, food_amount):
        if food_amount == 0:
            food_amount = 1
        global generator_int
        generator_int = generator_int / food_amount
        if random.randint(0, 1000) < generator_int:
            food_dot = turtle.Turtle()
            food_dot.shape("circle")
            food_dot.color("red")
            food_dot.penup()
            food_dot.shapesize(0.2)
            x = random.randint(int(-(self.screen.window_width() / 2)), int(self.screen.window_width() / 2))
            y = random.randint(int(-(self.screen.window_height() / 2)), int(self.screen.window_height() / 2))
            food_dot.sety(y)
            food_dot.setx(x)
            self.food_array.append(food_dot)
            generator_int = 1
        else:
            generator_int += 1

    def is_food_close(self, snake_head: turtle.Turtle()):
        answer = False
        x = snake_head.xcor()
        y = snake_head.ycor()
        for dot in self.food_array:
            if x + 5 > dot.xcor() > x - 5:
                if y + 5 > dot.ycor() > y - 5:
                    answer = True
                    break
        return answer

    def eat_a_food_dot(self, x: float, y: float):
        for i in range(len(self.food_array)):
            if x + 10 > self.food_array[i].xcor() > x - 10 and y + 10 > self.food_array[i].ycor() > y - 10:
                self.food_array[i].hideturtle()
                del self.food_array[i]
                break
