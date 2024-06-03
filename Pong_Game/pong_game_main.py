from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddles()
r_paddle.create_paddle(380, 0)

l_paddle = Paddles()
l_paddle.create_paddle(-387, 0)

ball = Ball()
ball.create_ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True
ball_bounced = False

while game_on is True:
    time.sleep(1/20)
    screen.update()
    ball.move_ball()


    # Detects collision with wall
    if ball.y_cor() > 280 or ball.y_cor() < -280:
        ball.bounce_y()
        ball_bounced = False

    # Detects collision with right paddle
    if ball.ball.distance(r_paddle.paddle) < 55 and ball.x_cor() > 350:
        if ball.x_cor() < 380:
            if ball_bounced is False:
                ball.bounce_x()
                ball_bounced = True

    # Detects collision with left paddle
    if ball.ball.distance(l_paddle.paddle) < 55 and ball.x_cor() < -360:
        if ball.x_cor() > - 387:
            if ball_bounced is False:
                ball.bounce_x()
                ball_bounced = True


    # Detects right paddle miss
    if ball.x_cor() > 400:
        ball.reset_position()
        score.l_point()

    # Detects left paddle miss
    if ball.x_cor() < -405:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
