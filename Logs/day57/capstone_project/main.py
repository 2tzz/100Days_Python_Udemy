from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/2ad2d2fb73e1aa796f90'
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()   
    return render_template("index.html" , posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)
