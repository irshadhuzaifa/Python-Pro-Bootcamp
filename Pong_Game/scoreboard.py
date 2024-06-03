from turtle import Turtle

Font = ("Cambria", 24, "normal")

class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="left", font = Font)
        self.goto(100, 250)
        self.write(self.r_score, align="left", font = Font)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

