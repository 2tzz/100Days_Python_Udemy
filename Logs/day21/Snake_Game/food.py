from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.random_color())  # Set the color using normalized RGB values
        self.refresh()

    def refresh(self):
        self.color(self.random_color()) 
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def random_color(self):
        r = random.randint(0, 255) / 255.0  # Normalize RGB values to [0, 1]
        g = random.randint(0, 255) / 255.0
        b = random.randint(0, 255) / 255.0
        color_tuple = (r, g, b)  # Return normalized RGB tuple
        return color_tuple