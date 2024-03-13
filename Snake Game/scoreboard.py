from turtle import Turtle

Font: tuple[str, int, str] = ("Cambria", 24, "normal")
Alignment = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.score = 0
        self.penup()
        self.goto(-220, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=Alignment, font=Font)
