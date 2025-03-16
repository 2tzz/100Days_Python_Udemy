from turtle import Turtle , Screen

turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
turtle.width(2)
turtle.speed(15)

screen.screensize(800, 800)

col = ('white', 'lightgreen' ,'limegreen')
for i in range (300):
    turtle.pencolor(col[i%3])
    turtle.forward(i * 3)
    turtle.right(121)


screen.exitonclick()