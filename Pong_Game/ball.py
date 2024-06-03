from turtle import Turtle

class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.x_move = 10
        self.y_move = 10



    def create_ball(self):
        self.ball.shape("circle")
        self.ball.color("yellow")
        self.ball.penup()



    def move_ball(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def x_cor(self):
        return self.ball.xcor()

    def y_cor(self):
        return self.ball.ycor()

    def reset_position(self):
        self.ball.goto(0,0)
        self.bounce_x()