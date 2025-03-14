import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = 0

carmanager = CarManager()
player = Player()
scoreboard =  Scoreboard ()


screen.listen()
screen.onkey(player.go , "Up" )

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    carmanager.add_car()
    carmanager.car_fd()

    for car in carmanager.cars:

        if car.distance(player) < 20 :
            game_is_on = False

    if player.is_at_finish() :
        player.reset_me()
        carmanager.level_up()
        scoreboard.increse_level()
        scoreboard.update_scoreboard()
    

screen.exitonclick()
    
    
