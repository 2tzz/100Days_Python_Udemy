from turtle import Turtle

class Paddel(Turtle) :

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1 , 5)
        self.left(90)
        self.color("White")

    def go_to (self , x , y):
        self.penup()
        self.teleport(x , y)

    def go_up (self):
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)
    
    def go_down (self):
        new_y = self.ycor() - 20
        self.goto(self.xcor() , new_y)