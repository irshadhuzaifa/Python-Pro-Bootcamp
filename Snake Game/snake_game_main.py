from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width =600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


my_snake = Snake()
my_snake.create()

food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")

game_on = True
while game_on is True:
    my_snake.move()
    screen.update()
    time.sleep(0.1)

    # Detect collision with food.
    if my_snake.segments[0].distance(food)<15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280 or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].ycor() < -280:
        game_on = False
        scoreboard.gameover()

    # Detect collision with tail.
    for segment in my_snake.segments:
        if segment == my_snake.segments[0]:
            pass
        elif my_snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.gameover()

screen.exitonclick()