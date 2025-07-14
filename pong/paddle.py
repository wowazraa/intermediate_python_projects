from turtle import *

class Paddle:
    def __init__(self, xcor, ycor):
        self.segments = []
        self.create_paddle(xcor, ycor)

    def create_paddle(self, xcor, ycor):
        for _ in range(5):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(xcor, ycor)
            self.segments.append(segment)
            ycor += 20

    def go_up(self):
        for seg in self.segments:
            seg.sety(seg.ycor() + 20)

    def go_down(self):
        for seg in self.segments:
            seg.sety(seg.ycor() - 20)
