from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 200)
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score2} | {self.score1} ", align=ALIGNMENT, font=FONT)

    def add_score1(self):
        self.clear()
        self.score1 += 1
        self.update_score()

    def add_score2(self):
        self.clear()
        self.score2 += 1
        self.update_score()
