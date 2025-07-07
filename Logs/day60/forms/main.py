from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html" )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("sucess.html" )
    

# @app.route('/about')
# def about_page():
#     return render_template("about.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
   