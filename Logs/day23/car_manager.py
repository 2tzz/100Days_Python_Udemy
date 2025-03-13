from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1 , 2)
        self.penup()
        self.setheading(180)
        
    def stating_pos(self):

        self.goto(280 , 0)
