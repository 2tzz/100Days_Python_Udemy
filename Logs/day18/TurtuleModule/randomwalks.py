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



timmy_the_tutle.shape("classic")
timmy_the_tutle.shapesize(1,1)

timmy_the_tutle.speed(8)
timmy_the_tutle.pensize(10)

for i in range (0 , random.randint(150,200)) :

    timmy_the_tutle.forward(20 *random.randint( 1 , 3) )
    timmy_the_tutle.right(90 * random.randint(-1 , 3))
  
    timmy_the_tutle.color(random_color())



screen = Screen ()
screen.exitonclick ()