from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def greet_fast(name):
    return f"Hellow there {name} ! "

@app.route("/username/<name>/<int:number>")
def greet(name , number):
    return f"Hellow {name} ,you are {number} years old ! "

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

if __name__ == "__main__" :
    #run in debug mode to auto run server whenever makes a change
    app.run(debug=True)