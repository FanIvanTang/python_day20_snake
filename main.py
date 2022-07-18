from turtle import Screen
from food import Food
from snake import Snake
import time
from scoreboard import Scoreboard

TIME_OF_REFREASH = 0.2

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Ivan's Snake Game")

s.tracer(0)

snake = Snake()

food = Food()

scoreboard = Scoreboard()


s.listen()
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")


game_is_on = True

while game_is_on:

    s.update()
    time.sleep(TIME_OF_REFREASH)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.eat_food()
        scoreboard.add_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False

    for t in snake.body:

        if t == snake.head:
            pass
        elif snake.head.distance(t) < 10:
            game_is_on = False


scoreboard.gameover()


s.exitonclick()
