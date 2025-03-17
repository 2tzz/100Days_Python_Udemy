from turtle import Turtle
import random

highlight_colors = [
    (57/255, 255/255, 20/255),   # Neon Green
    (0/255, 191/255, 255/255),   # Electric Blue
    (255/255, 20/255, 147/255),  # Hot Pink
    (225/255, 255/255, 0/255),   # Lime Yellow
    (0/255, 255/255, 255/255),   # Cyan Glow
    (180/255, 255/255, 200/255), # Soft Mint
    (173/255, 216/255, 230/255), # Baby Blue
    (255/255, 218/255, 185/255), # Peach Glow
    (230/255, 230/255, 250/255), # Lavender Light
    (255/255, 165/255, 100/255), # Sunset Orange
    (255/255, 223/255, 0/255),   # Golden Glow
    (245/255, 222/255, 179/255), # Warm Beige
    (255/255, 191/255, 0/255)    # Amber Light
]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.random_color())  # Set the color using normalized RGB values
        self.refresh()

    def refresh(self):
        self.color(random.choice(highlight_colors)) 
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def random_color(self):
        r = random.randint(0, 255) / 255.0  # Normalize RGB values to [0, 1]
        g = random.randint(0, 255) / 255.0
        b = random.randint(0, 255) / 255.0
        color_tuple = (r, g, b)  # Return normalized RGB tuple
        return color_tuple
    
