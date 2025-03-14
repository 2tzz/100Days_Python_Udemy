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

carmanager.create_cars()

screen.listen()
screen.onkey(player.go , "Up" )

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    for i in range(0,10) :
            if carmanager.cars[i].distance(player) < 30 :
                 game_is_on = False
                 
            if carmanager.cars[i].xcor() < -280 :
                carmanager.cars[i].goto(random.randint(280 , 500) , random.randint(-280,280) )
            carmanager.cars[i].forward(10)

    screen.update()


screen.exitonclick()
    
    
