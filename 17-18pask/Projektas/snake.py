import turtle
import turtle as t
t.Screen().colormode(255)


class Snake:
    def __init__(self, screen: t.Screen()):
        self.snake_body = [t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(),
                           t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(),
                           t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(),
                           t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle()]
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
            self.snake_body[x].setx(self.snake_body[x - 1].xcor())
            self.snake_body[x].sety(self.snake_body[x - 1].ycor())
        self.snake_body[0].forward(8)
        self.screen.update()

    def turn_left(self):
        self.snake_body[0].setheading(self.snake_body[0].heading() + 90)

    def turn_right(self):
        self.snake_body[0].setheading(self.snake_body[0].heading() - 90)

    def check_bounds(self):
        if self.snake_body[0].xcor() > (self.screen.window_width() / 2):
            return True
        elif self.snake_body[0].xcor() < -(self.screen.window_width() / 2):
            return True
        elif self.snake_body[0].ycor() > (self.screen.window_height() / 2):
            return True
        elif self.snake_body[0].ycor() < -(self.screen.window_height() / 2):
            return True

    def generate_snake_body(self):
        new_body_part = turtle.Turtle()
        new_body_part.penup()
        new_body_part.setx(self.snake_body[len(self.snake_body) - 1].xcor())
        new_body_part.sety(self.snake_body[len(self.snake_body) - 1].ycor())
        new_body_part.shape("circle")
        new_body_part.shapesize(0.4)
        new_body_part.color(45, 120, 45)
        self.snake_body.append(new_body_part)

    def check_if_snake_overlaps(self):
        for snake_body_part in self.snake_body:
            for snake_body_part2 in self.snake_body:
                if snake_body_part == snake_body_part2:
                    break
                else:
                    if snake_body_part.xcor() + 1 > snake_body_part2.xcor() > snake_body_part.xcor() - 1:
                        if snake_body_part.ycor() + 1 > snake_body_part2.ycor() > snake_body_part.ycor() - 1:
                            return True
        return False
