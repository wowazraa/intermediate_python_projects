import random
from turtle import *

screen = Screen()

colors = ["blue", "red", "orange", "green", "pink", "black"]
y_positions = [-100, -60, -20, 20, 60, 100]
steps = [1, 2, 3, 4, 5]

turtles = []
stop = False

screen.setup(500, 400)
user_bet  = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.teleport(-230, y_positions[turtle_index])
    tim.color(colors[turtle_index])
    turtles.append(tim)

while not stop:
    for t in turtles:
        t.forward(random.choice(steps))
        if t.xcor() >= 200:
            winner_turtle = colors[turtles.index(t)]
            stop = True
            break

if winner_turtle == user_bet.lower():
    print(f"You win! Winner is {winner_turtle} one.")
else:
    print(f"You lose! Winner is {winner_turtle} one.")

screen.exitonclick()
