from turtle import Turtle , Screen
import random

timmy_the_tutle = Turtle ()


# timmy_the_tutle.shape("turtle")

timmy_the_tutle.shape("circle")
timmy_the_tutle.shapesize(1,1)

timmy_the_tutle.color("Red")

timmy_the_tutle.speed(1)
sides = 1

color_list = [
    "red", "green", "blue", "yellow", "orange", 
    "purple", "pink", "brown", "gray", "black", 
    "white", "cyan", "magenta", "lime", "teal", 
    "navy", "gold", "silver", "maroon", "olive", 
    "coral", "salmon", "turquoise", "indigo", "violet", 
    "beige", "lavender", "peach", "skyblue", 
    "chocolate", "tomato", "orchid", "plum", "slateblue", 
    "darkgreen", "lightgreen", "darkblue", "lightblue", "darkred", 
    "hotpink", "deeppink", "mediumpurple", "lightcoral", "darkorange", 
    "lightsalmon", "darkslategray", "lightslategray", "mediumslateblue", "palegreen"
]


for i in range(3,11) :
    turn_angle = 360 / i
    
    color = random.choice(color_list)
    print(color)
    timmy_the_tutle.color(color)

    for j in range (i) :

        timmy_the_tutle.forward(100)
        timmy_the_tutle.right(turn_angle)

    



screen = Screen ()
screen.exitonclick ()