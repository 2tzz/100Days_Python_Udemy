from turtle import  Screen
from paddel import Paddel

paddel = Paddel()

game_is_on = True

screen = Screen ()
screen.bgcolor("black")
screen.setup(width=800 ,height=600)
screen.title("My Pong Game")
screen.tracer(0)


screen.listen()
screen.onkey(paddel.go_up ,"Up")
screen.onkey(paddel.go_down ,"Down")

paddel.go_to()


while game_is_on :
    screen.update()





































screen.exitonclick()