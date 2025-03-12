from turtle import Turtle

class Paddel(Turtle) :

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1 , 5)
        self.left(90)
        self.color("White")

    def go_to (self):

        self.penup()
        self.teleport(383 , 0)

    def go_up (self):
        self.forward(20)
    
    def go_down (self):
        self.backward(20)
