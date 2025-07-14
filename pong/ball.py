from paddle import *

class Ball(Turtle):
    def __init__(self, scoreboard):
        super().__init__()
        self.scoreboard = scoreboard
        self.add_ball()
        self.x_move = 15
        self.y_move = 15

    def add_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_updown(self):
        if not 280 >= self.ycor() >= -280:
            self.y_move *= -1

    def collision_paddle(self, paddle):
        for segment in paddle.segments:
            if self.distance(segment) < 20:
                self.x_move *= -1
                break

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1

    def collision_score(self):
        if 380 < self.xcor():
            self.scoreboard.l_point()
            self.reset_position()
        elif self.xcor() < -380:
            self.scoreboard.r_point()
            self.reset_position()



