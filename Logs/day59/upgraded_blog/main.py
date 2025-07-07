from flask import Flask, render_template
import requests


response = requests.get('https://api.npoint.io/e6eb6f957cc456f84ab9')
response.raise_for_status()
all_posts = response.json()


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html" ,  posts = all_posts)

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/about')
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
   