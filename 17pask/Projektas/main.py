import turtle as t
import snake


screen = t.Screen()
screen.setup(700, 700)
screen.tracer(0)
snake = snake.Snake(screen)
screen.listen()
screen.onkey(snake.turn_left, "a")

program_is_running = True
while program_is_running:
    screen.ontimer(snake.forward_snake_move(), 100)


screen.exitonclick()
