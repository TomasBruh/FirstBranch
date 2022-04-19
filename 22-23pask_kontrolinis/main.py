import turtle as t
import bird
import pipes

screen = t.Screen()
screen.setup(500, 500)
screen.tracer(0)

birdie = bird.Bird(screen)


def jump():
    # birdie.bird.sety(birdie.bird.ycor() + 50)
    birdie.bird_fall = -5
    for _ in range(10):
        birdie.jump(1.5)
        birdie.bird.heading() + 10
        screen.update()
    for _ in range(10):
        birdie.jump(1.7)
        screen.update()
    for _ in range(10):
        birdie.jump(1.5)
        screen.update()
    for _ in range(10):
        birdie.jump(1.2)
        screen.update()
    for _ in range(10):
        birdie.jump(1.1)
        screen.update()
    for _ in range(10):
        birdie.jump(1)
        screen.update()
    for _ in range(10):
        birdie.jump(0.5)
        screen.update()
    for _ in range(100):
        birdie.jump(0.2)
        screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
    # for _ in range(10):
    #     birdie.jump(1)
    #     screen.update()
# PUT IN CLASS ^


test_pipe = pipes.Pipe(screen)

screen.onkey(jump, " ")
screen.listen()
game_is_running = True

while game_is_running:
    screen.ontimer(birdie.gravity_fall(), 20)
    if birdie.is_flying() is False:
        break
    screen.update()

