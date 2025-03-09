from turtle import Turtle , Screen


screen = Screen ()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x = 0
y = 0


for turtle in range (0,3) :
    

    new_turtle = Turtle(shape="square")
    new_turtle.color("White")
    new_turtle.penup()
    new_turtle.shapesize(1 , 1)
    new_turtle.teleport (x , y)

    x += 20
















screen.exitonclick()