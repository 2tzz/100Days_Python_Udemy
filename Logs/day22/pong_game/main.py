from turtle import  Screen 
from paddel import Paddel
from ball import Ball
from score import Score
import time


paddel = Paddel()
paddel2 = Paddel ()
ball = Ball ()
score = Score ()
score2 = Score ()
over = Score()


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

r_score = 0
l_score = 0


while game_is_on :

    screen.update()
    time.sleep(0.005)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.ball_collision()
    if ball.distance(paddel)  <= 40 and ball.xcor() >  370:
        ball.ball_collision()
    if ball.distance(paddel2) <= 50 and ball.xcor() <  -370:
        ball.ball_collision()
    if ball.xcor() > 396 :
        time.sleep(1)
        ball.ball_reset()
        l_score += 1
        score.draw_score_l(l_score)

    if ball.xcor() < -402 :
        time.sleep(1)
        ball.ball_reset()  
        r_score += 1 
        score2.draw_score_r(r_score)
    
    if r_score == 10 or l_score ==10 :

        if r_score > l_score :

            over.game_over("Right")
            game_is_on = False
        
        elif r_score < l_score :

            over.game_over("Left")
            game_is_on = False

   





































screen.exitonclick()