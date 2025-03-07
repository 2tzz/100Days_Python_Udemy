from turtle import Turtle, Screen
import random

refree = Turtle()
refree.ht()


screen = Screen()
screen.setup(width = 500 ,height =  400)

colors = ["red","orange","yellow","green","blue"]

y = -100



# tim = Turtle(shape="turtle" )
# tim.color("Red")

# blue = Turtle(shape="turtle" )
# blue.color("Blue")

# green = Turtle(shape="turtle" )
# green.color("green")

# yellow = Turtle(shape="turtle" )
# yellow.color("Yellow")

# purple = Turtle(shape="turtle" )
# purple.color("Purple")


def draw_finishline():

    refree.teleport (230 , -120)
    refree.pencolor("DarkRed")
    refree.pensize(10)
    refree.left(90)
    refree.forward(240)

# def teleport_to_start():
#     tim.teleport(-230, -100)
#     blue.teleport(-230, -50)
#     green.teleport(-230, 0)
#     yellow.teleport(-230, 50)
#     purple.teleport(-230, 100)

# def turtle_run ():

#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0

#     distance = 40

#     speed = 1

#     tim.speed(speed)
#     blue.speed(speed)
#     green.speed(speed)
#     yellow.speed(speed)
#     purple.speed(speed)

#     while a <= distance or b <= distance or c <= distance or d <= distance or e <= distance :

#         a += random.randint(1 ,5)
#         b += random.randint(1 ,5)
#         c += random.randint(1 ,5)
#         d += random.randint(1 ,5)
#         e += random.randint(1 ,5)

        

#         tim.forward(a)
#         blue.forward(b)
#         green.forward(c)
#         yellow.forward(d)
#         purple.forward(e)

        







for i in range(0 , 5) :

    
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.teleport(-230, y)
    y += 50


draw_finishline ()


screen.exitonclick()