from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != UP:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != DOWN:
            self.head.setheading(DOWN)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
