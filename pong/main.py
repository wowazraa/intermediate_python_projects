from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball(scoreboard)
r_paddle = Paddle(xcor=350, ycor=-40)
l_paddle = Paddle(xcor=-350, ycor=-40)

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # detect collision with up and down walls
    ball.collision_updown()

    # detect collision with paddles
    ball.collision_paddle(r_paddle)
    ball.collision_paddle(l_paddle)

    # check score
    ball.collision_score()

screen.exitonclick()
