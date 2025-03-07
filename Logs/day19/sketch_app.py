from turtle import Turtle , Screen

tim = Turtle ()

screen = Screen()


def move_forward () :
    tim.forward(20)

def move_backward ():
    tim.back(20)

def turn_clockwise ():
    tim.right(30)

def turn_counter_clockwise ():
    tim.left(30)

def clear_drawing():
    tim.reset()



screen.listen()
screen.onkey(key = "w", fun =move_forward)
screen.onkey(key = "s", fun =move_backward)
screen.onkey(key = "d", fun =turn_clockwise)
screen.onkey(key = "a", fun =turn_counter_clockwise)
screen.onkey(key = "c", fun =clear_drawing)


screen.exitonclick()
