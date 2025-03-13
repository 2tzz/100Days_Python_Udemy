from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    

    def __init__(self):
        

        self.cars = []
        

    def create_cars (self):
        for car in range(0,10) :
            self.add_car((random.randint(280 , 500) , random.randint(-280,280)))

  

    def add_car (self , position):
        new_car = Turtle ()
        new_car.shape("square")
        new_car.shapesize(1 , 2)
        new_car.penup()
        new_car.setheading(180)
        new_car.color(COLORS[random.randint(0,5)])
        new_car.goto(position)
        self.cars.append(new_car)
    
    def car_fd(self):

        for i in range(0,10) :
            if self.cars[i].xcor() < -280 :
                self.cars[i].goto(random.randint(280 , 500) , random.randint(-280,280) )
            self.cars[i].forward((MOVE_INCREMENT))
            
