import turtle as t
import snake
import food

screen = t.Screen()
screen.setup(500, 500)
screen.tracer(0)
snake = snake.Snake(screen)
food = food.Food(screen)
screen.listen()
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

program_is_running = True
while program_is_running:
    if snake.check_bounds():
        program_is_running = False
        break
    if snake.check_if_snake_overlaps():
        program_is_running = False
    if food.is_food_close(snake.snake_body[0]):
        food.eat_a_food_dot(snake.snake_body[0].xcor(), snake.snake_body[0].ycor())
        snake.generate_snake_body()
    screen.ontimer(snake.forward_snake_move(), 50)
    food.generate_food(len(food.food_array))


screen.exitonclick()
