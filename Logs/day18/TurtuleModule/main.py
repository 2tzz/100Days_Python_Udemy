from turtle import Turtle , Screen

timmy_the_tutle = Turtle ()


timmy_the_tutle.shape("turtle")


timmy_the_tutle.speed(1)

i = 0
while i < 100 :

    if i == 5 :
        timmy_the_tutle.right(90)
    if i == 10 :
        timmy_the_tutle.right(90)
    if i == 20  :
        timmy_the_tutle.right(90)
    if i == 30  :
        timmy_the_tutle.right(90)

    timmy_the_tutle.forward(10)
    timmy_the_tutle.penup()
    timmy_the_tutle.forward(10)
    timmy_the_tutle.pendown()
    timmy_the_tutle.forward(10)
    timmy_the_tutle.penup()
    timmy_the_tutle.forward(10)
    timmy_the_tutle.pendown()
    timmy_the_tutle.forward(10)
    timmy_the_tutle.penup()
    timmy_the_tutle.forward(10)
    timmy_the_tutle.pendown()
    i += 1




screen = Screen ()
screen.exitonclick ()




