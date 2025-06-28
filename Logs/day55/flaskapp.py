from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<h1 style= 'text-align : center ' >Hello, World! </h1>" \
    "<p>this is a paragraph text</p>" \
    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3Y1Y2gyMDl1NjR3cGZzaW53eGozc2Y4dHF0ZXl1eGR4Z2lvNGh2OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/njtPBlbYnHAHK/giphy.gif' width=200>"


