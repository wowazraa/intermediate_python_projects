from turtle import *

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()

    def create_level(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def create_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
