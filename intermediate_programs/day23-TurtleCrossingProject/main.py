# Elvin Rivera
# 8/6/2021

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
    time.sleep(0.1)     # everything inside this loop will be refreshed at that rate
    screen.update()

    car_manager.create_car()        # creates new car every 0.1 second
    car_manager.move_cars()     # moves car every 0.1 second

    # Detect collision with car, .all_cars is the list defined in car_manager
    for car in car_manager.all_cars:
        # .distance compares distance between two things
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()      # call function to increase speed
        scoreboard.increase_level()

screen.exitonclick()
