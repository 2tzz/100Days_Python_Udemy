from turtle import  Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time
import random


screen = Screen ()
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food ()
scoreboard = ScoreBoard ()
scoreboard2 = ScoreBoard ()

scoreboard2.draw_boundry()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right ,"Right")

game_is_on = True

snake.create_snake()

while game_is_on :
    scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colution with snake

    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increse_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 265 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()
        
        

    for segment in snake.segments[1:]:
    
        if snake.head.distance(segment) < 8:
            scoreboard.reset()
            snake.reset()
            


    











screen.exitonclick()