import turtle as t
import random
t.register_shape("pipe.gif")
t.register_shape("pipe1.gif")
t.register_shape("pipe_upsidedown1.gif")


class Pipe:
    def __init__(self, screen: t.Screen(), ycor, name):
        pipe = t.Turtle()
        pipe.color("green")
        pipe.penup()
        pipe.setx(screen.window_width() / 2)
        pipe.shape(name)
        pipe.sety(ycor)
        self.inner_pipe = pipe


class Pipes:
    def __init__(self, screen: t.Screen()):
        self.screen = screen
        self.pipes = [[], []]
        self.time_to_spawn = 50

    def add_pipes(self):
        random_y0 = random.randint(self.screen.window_height() / 2, self.screen.window_height() / 2 - 100)
        random_y1 = self.screen.window_height() - random_y0
        if self.time_to_spawn == 0:
            self.pipes[0].append(Pipe(self.screen, self.screen.window_height() / 2, "pipe_upsidedown1.gif"))
            self.pipes[1].append(Pipe(self.screen, -(self.screen.window_height() / 2), "pipe1.gif"))
            self.time_to_spawn = 25
        else:
            self.time_to_spawn = self.time_to_spawn - 1

    def move_remove_pipes(self):
        for pipe in self.pipes[0]:
            pipe.inner_pipe.setx(pipe.inner_pipe.xcor() - 10)
            if pipe.inner_pipe.xcor() < -(self.screen.window_width() / 2) - 20:
                self.pipes[0].remove(pipe)
        for pipe in self.pipes[1]:
            pipe.inner_pipe.setx(pipe.inner_pipe.xcor() - 10)

        self.screen.update()

    def check_if_bird_crashed(self, bird: t.Turtle):
        for pipe in self.pipes[0]:
            if pipe.inner_pipe.distance(bird) < 100:
                return True
            # if bird.distance(pipe.inner_pipe.xcor(), pipe.inner_pipe.ycor() + 110) < 50:
            #     return True
        for pipe in self.pipes[1]:
            if pipe.inner_pipe.distance(bird) < 100:
                return True
        return False
