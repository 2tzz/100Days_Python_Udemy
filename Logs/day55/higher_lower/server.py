from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0,10)

@app.route("/")
def higher_lower():
    return "<h1 style= 'text-align : left ' >Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>" \
    f"<p>{random_num}</p>"

@app.route("/<int:number>")
def check_number(number):
    if number == random_num:
        return "<h1 style= 'color : green ' >You Found me</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200>"
    elif number > random_num :
        return "<h1 style= 'color : purple ' >Too high</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200>"
    elif number < random_num :
        return "<h1 style= 'color : red ' >Too low</h1>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200>"

if __name__ == "__main__" :
    #run in debug mode to auto run server whenever makes a change
    app.run(debug=True)

