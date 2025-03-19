import turtle
import pandas


screen = turtle.Screen()
pen = turtle.Turtle()

screen.title("U.S. States")


image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
guessed_states = []




i = 0

while i < 50 :

    user_guess = screen.textinput(title=f"Make Yor Guess    {i}/50 correct ", prompt="What are the states in U.S. ? :").title()

    if user_guess == "Exit" :

        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states :
        if user_guess == state :

            guessed_states.append(user_guess)
            pen.ht()
            pen.penup()
            state_data = data[data.state == user_guess]
            pen.goto(state_data.x.item() ,state_data.y.item() )
            pen.write(user_guess)

            

            i += 1




