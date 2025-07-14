from turtle import *

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)

