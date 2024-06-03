from turtle import Turtle

class Paddles:


    def __init__(self) -> object:
        self.paddle = Turtle()




    def create_paddle(self, x, y):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.turtlesize(stretch_len=5, stretch_wid=1)
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.goto(x, y)


    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)


    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


    def y_cor(self):
        return self.paddle.ycor()

    def x_cor(self):
        return self.paddle.xcor()