# import colorgram
# import os

# # Get the directory where the script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct the full path to the image file
# image_path = os.path.join(script_dir, 'hi.jpg')

# # Extract colors
# colors = colorgram.extract(image_path, 30)



# color_list = []

# for _ in colors :
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b

#     new_color = (r , g , b)

#     color_list.append(new_color)


color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),(17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

import turtle as t
from turtle import Screen

import random

timmy = t.Turtle ()
t.colormode(255)


def random_color():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color_tuple = (r ,g ,b)

    return color_tuple

y = -250
x =  -300

timmy.ht()
timmy.speed(0)

for i in range(10):
    for j in range(10):

        x += 50
        timmy.teleport(x , y )
        # timmy.color("White" , random.choice(color_list))
        # timmy.begin_fill()
        # timmy.circle(10)
        # timmy.end_fill()
        timmy.dot(20 , random.choice(color_list) )

    x = -300
    y += 50

screen = Screen ()
screen.exitonclick ()