from turtle import  Screen
from paddel import Paddel
from ball import Ball
import time

paddel = Paddel()
paddel2 = Paddel ()
ball = Ball ()

game_is_on = True

screen = Screen ()
screen.bgcolor("black")
screen.setup(width=800 ,height=600)
screen.title("My Pong Game")
screen.tracer(0)


screen.listen()
screen.onkey(paddel.go_up ,"Up")
screen.onkey(paddel.go_down ,"Down")
screen.onkey(paddel2.go_up ,"w")
screen.onkey(paddel2.go_down ,"s")

paddel.go_to(380 , 0)
paddel2.go_to(-390 , 0)


while game_is_on :
    screen.update()
    time.sleep(0.005)

    ball.move()





































screen.exitonclick()