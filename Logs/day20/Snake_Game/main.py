from turtle import Turtle , Screen
import time


screen = Screen ()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x = 0
y = 0


starting_positions = [(0,0) , (-20,0) ,(-40,0)]
segments  = []

for positions in  starting_positions :
    

    new_turtle = Turtle(shape="square")
    new_turtle.color("White")
    new_turtle.penup()
    new_turtle.goto(positions)
    segments.append(new_turtle)
    


game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)
    
    for  seg_num in range (len(segments) - 1, 0 , -1) :
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)

    segments[0].forward(20)
    
        













screen.exitonclick()