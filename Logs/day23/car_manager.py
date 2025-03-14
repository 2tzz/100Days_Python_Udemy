from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    

    def __init__(self):
        
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def add_car (self ):
        random_chance = random.randint(1,6)

        if random_chance == 1:
            new_car = Turtle ()
            new_car.shape("square")
            new_car.shapesize(1 , 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto((random.randint(280 , 500) , random.randint(-280,280)))
            self.cars.append(new_car)
        
    def car_fd(self):

        for car in self.cars :
            car.forward(self.car_speed)

    def level_up(self):

        self.car_speed += MOVE_INCREMENT
