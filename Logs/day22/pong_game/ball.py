from turtle import Turtle

class Ball(Turtle) :
    
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(1 , 1)
        self.penup()


    def move(self):
        new_x = self.xcor()+1
        new_y = self.ycor()+1
        self.goto(new_x ,new_y)

    # def ball_collution (self , x , y):


