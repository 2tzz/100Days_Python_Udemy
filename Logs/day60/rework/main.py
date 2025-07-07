from flask import Flask, render_template
import requests


response = requests.get('https://api.npoint.io/1df9a2e468e2408de0fc')
response.raise_for_status()
posts = response.json()


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html" ,  posts = posts)

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route("/post/<int:num>")
def get_blogs(num):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
   