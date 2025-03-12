from turtle import Turtle
import random

class Ball(Turtle) :
    
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(1 , 1)
        self.penup()
        self.setheading(45)


    def move(self):
        
        self.forward(1)

    def ball_collision (self):

        self.color(self.random_color())  # Set the color using normalized RGB values
        self.setheading(self.heading() + 90)


    def ball_reset (self):
        self.teleport(0,0)
        self.setheading(self.heading() + random.randint(165 , 200))

    def random_color(self):
        r = random.randint(0, 255) / 255.0  # Normalize RGB values to [0, 1]
        g = random.randint(0, 255) / 255.0
        b = random.randint(0, 255) / 255.0
        color_tuple = (r, g, b)  # Return normalized RGB tuple
        return color_tuple

        


