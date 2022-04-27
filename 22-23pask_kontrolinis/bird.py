import turtle as t
t.register_shape("regular.gif")
t.register_shape("rotated10.gif")
t.register_shape("rotated15.gif")
t.register_shape("rotated20.gif")
t.register_shape("rotated340.gif")
t.register_shape("rotated350.gif")
t.register_shape("rotated355.gif")


class Bird:
    def __init__(self, screen: t.Screen()):
        t.mode("logo")
        birdie = t.Turtle()
        birdie.color("orange")
        birdie.shape("regular.gif")
        birdie.penup()
        birdie.speed("slowest")
        birdie.sety(birdie.ycor() + 100)
        self.bird = birdie
        self.bird_fall = 10
        self.bird_fall_multi = 1
        self.screen = screen

    def gravity_fall(self):
        self.bird.sety(self.bird.ycor() - int(self.bird_fall * self.bird_fall_multi))
        # if self.bird_fall < 10:
        self.bird_fall = self.bird_fall + 0.01
        # if self.bird_fall_multi < 1:
        self.bird_fall_multi = self.bird_fall_multi + 0.02
        self.screen.update()
        # if self.bird_fall > 0:
        #     self.bird.shape("rotated10.gif")
        # if self.bird_fall > 10:
        #     self.bird.shape("rotated15.gif")
        # if self.bird_fall > 10:
        #     self.bird.shape("rotated20.gif")

    def is_flying(self):
        if self.bird.ycor() < -(self.screen.window_height() / 2) + 20:
            return False
        return True

    def jump(self):
        # if not self.bird_fall < 0:
        #     self.bird_fall = -1
        self.bird_fall_multi = 0.1
        self.bird.forward(100)

