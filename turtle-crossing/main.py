import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.create_level()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.create_game_over()
            break

    if not 280 >= player.ycor() >= -280:
        scoreboard.clear()
        scoreboard.score += 1
        car_manager.increase_speed()
        player.goto(0, -280)

screen.exitonclick()

