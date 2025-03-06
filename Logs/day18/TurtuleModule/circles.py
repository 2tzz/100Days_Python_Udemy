import turtle as t
from turtle import Screen

import random

timmy_the_tutle = t.Turtle ()
t.colormode(255)


def random_color():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color_tuple = (r ,g ,b)

    return color_tuple


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        timmy_the_tutle.color(random_color())
        timmy_the_tutle.circle(100)
        timmy_the_tutle.setheading(timmy_the_tutle.heading() + size)



timmy_the_tutle.shape("classic")
timmy_the_tutle.shapesize(1,1)

timmy_the_tutle.speed(0)
timmy_the_tutle.pensize(2)

# my implement

# for i in range (10) :

#     for j in range(36):
#         timmy_the_tutle.forward(20)
#         timmy_the_tutle.right(10)
#     timmy_the_tutle.right(36)
#     timmy_the_tutle.color(random_color())


# course implement


# for i in range (10) :

#     timmy_the_tutle.circle(100)
    
#     currunt_headding = timmy_the_tutle.heading()
#     timmy_the_tutle.setheading(currunt_headding + 36)
#     timmy_the_tutle.color(random_color())

draw_spirograph(10)

screen = Screen ()
screen.exitonclick ()