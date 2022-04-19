import turtle as t


class Bird:
    def __init__(self, screen: t.Screen()):
        birdie = t.Turtle()
        birdie.color("orange")
        t.register_shape("download4.gif")
        birdie.shape("download4.gif")
        birdie.penup()
        birdie.speed("slow")
        birdie.sety(birdie.ycor() + 100)
        self.bird = birdie
        self.bird_fall = 10
        self.bird_fall_multi = 1
        self.screen = screen

    def gravity_fall(self):
        self.bird.sety(self.bird.ycor() - int(self.bird_fall * self.bird_fall_multi))
        # if self.bird_fall < 10:
        self.bird_fall = self.bird_fall + 1
        # if self.bird_fall_multi < 1:
        self.bird_fall_multi = self.bird_fall_multi + 0.05
        self.screen.update()

    def jump(self, distance):
        self.bird.sety(self.bird.ycor() + distance)
        self.bird_fall_multi = 0.1
        self.screen.update()

    def is_flying(self):
        if self.bird.ycor() < -(self.screen.window_height() / 2) + 20:
            return False
        return True
