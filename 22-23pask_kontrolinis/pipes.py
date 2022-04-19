import turtle as t


class Pipe:
    def __init__(self, screen: t.Screen()):
        pipe = t.Turtle()
        pipe.color("green")
        pipe.penup()
        pipe.setx(screen.window_width() / 2)
        pipe.shape("rectangle")
        self.Pype = pipe
