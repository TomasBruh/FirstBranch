import turtle as t
import bird
import pipes

screen = t.Screen()
screen.setup(600, 450)
screen.tracer(0)

birdie = bird.Bird(screen)

test_pipe = pipes.Pipes(screen)

screen.onkey(birdie.jump, "w")
screen.listen()
game_is_running = True

while game_is_running:
    screen.ontimer(birdie.gravity_fall(), 20)
    test_pipe.add_pipes()
    test_pipe.move_remove_pipes()
    if test_pipe.check_if_bird_crashed(birdie.bird):
        break
    if birdie.is_flying() is False:
        break
    screen.update()
