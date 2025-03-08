from turtle import Turtle, Screen
import random

refree = Turtle()
refree.ht()

is_race_on = False

screen = Screen()
screen.setup(width = 500 ,height =  400)
screen.bgcolor("grey")


colors = ["red","orange","yellow","green","blue"]

y = -100
all_turtles = []



def draw_finishline():

    refree.teleport (230 , -120)
    refree.pencolor("DarkRed")
    refree.pensize(10)
    refree.left(90)
    refree.forward(240)


for i in range(0 , 5) :
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
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