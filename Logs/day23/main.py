import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

car_manager.stating_pos()
game_is_on = True

while game_is_on:
    
    car_manager.forward(3)
    time.sleep(0.1)
    screen.update()
    
