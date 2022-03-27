import turtle as t
t.Screen().colormode(255)


class Snake:
    def __init__(self, screen: t.Screen()):
        self.snake_body = [t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle()]
        self.snake_body[0].shapesize(1.8)
        self.snake_body[0].color(45, 120, 45)  # 45, 150, 45
        self.snake_body[0].penup()
        for i in range(len(self.snake_body) - 1):
            self.snake_body[i + 1].penup()
            self.snake_body[i + 1].setx(self.snake_body[i].xcor() - 7)
            self.snake_body[i + 1].shape("circle")
            self.snake_body[i + 1].shapesize(0.4)
            self.snake_body[i + 1].color(45, 120, 45)
        self.snake_body[0].setx(self.snake_body[0].xcor() + 8)
        self.screen = screen
        screen.update()

    def forward_snake_move(self):

        for i in range(len(self.snake_body) - 1):
            x = len(self.snake_body) - i - 1
            print(x)
            self.snake_body[x].setx(self.snake_body[x - 1].xcor())
            self.snake_body[x].sety(self.snake_body[x - 1].ycor())
            self.screen.update()
        self.snake_body[0].forward(8)
        # if self.snake_body[0].heading() == 0:
        #     self.snake_body[1].setx(self.snake_body[0].xcor() - 15)
        # elif self.snake_body[0].heading() == 90:
        #     self.snake_body[1].sety(self.snake_body[0].ycor() - 15)
        # elif self.snake_body[0].heading() == 180:
        #     self.snake_body[1].setx(self.snake_body[0].xcor() + 15)
        # elif self.snake_body[0].heading() == 270:
        #     self.snake_body[1].sety(self.snake_body[0].ycor() + 15)
        self.screen.update()

    def turn_left(self):
        self.snake_body[0].setheading(self.snake_body[0].heading() + 90)
