from turtle import Turtle

class Paddel(Turtle) :

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(5 , 1)
        self.color("White")

    def go_to (self):

        self.penup()
        self.goto(383 , 0)