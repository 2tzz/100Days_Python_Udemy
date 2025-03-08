from turtle import Turtle, Screen
import random

refree = Turtle()
refree.ht()

is_race_on = False

screen = Screen()
screen.setup(width = 500 ,height =  400)


colors = ["red","orange","yellow","green","blue"]

y = -100
all_turtles = []


# new_turtle = Turtle(shape="turtle" )
# new_turtle.color("Red")

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
#     new_turtle.teleport(-230, -100)
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

#     new_turtle.speed(speed)
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

        

#         new_turtle.forward(a)
#         blue.forward(b)
#         green.forward(c)
#         yellow.forward(d)
#         purple.forward(e)

        


for i in range(0 , 5) :
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.teleport(-230, y)
    y += 50

    all_turtles.append(new_turtle)

draw_finishline ()

user_bet = screen.textinput(title="Make Yor Bet", prompt="witch turtle will win the race ? Enter a color :")

if user_bet:

    is_race_on = True

while is_race_on :

    for turtle in all_turtles :

        if turtle.xcor() > 230 :
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet ! the winning color was  {winning_color} ")
                is_race_on = False
            
            else:
                print(f"You've lost  the bet . winning color was {winning_color}")
                is_race_on = False


        random_distance =  random.randint(0 , 10)
        turtle.forward(random_distance)


screen.exitonclick()