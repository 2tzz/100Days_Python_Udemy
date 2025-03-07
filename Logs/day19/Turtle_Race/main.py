from turtle import Turtle, Screen

tim = Turtle(shape="turtle")
screen = Screen()


def turtle_run ():

    print("im runing")




screen.setup(width = 500 ,height =  400)

user_bet = screen.textinput("Make your Bet","Pick a color of your Turtle :")

tim.teleport(-230, -100)



screen.exitonclick()