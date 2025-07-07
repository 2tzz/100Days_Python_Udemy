import dotenv
import os
from flask import Flask, render_template , request
import requests
import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp.gmail.com"
my_email = "XXXXXX"
reciver_email = 'XXXXXX'
passkey = "XXXXXX"


response = requests.get('https://api.npoint.io/1df9a2e468e2408de0fc')
response.raise_for_status()
posts = response.json()


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html" ,  posts = posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message_text = request.form['message']
        text = "Yor Message sent successfully"
        mail_sub = f'Thiyura you have messge from {name}'

        email_message = f"""\
        You have a message from {name} !

        {message_text}

        From: {email}
        Phone number: {phone}
        """
        message = MIMEText(email_message, "plain")
        message["Subject"] = mail_sub
        message["From"] = my_email
        message["To"] = reciver_email


        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(my_email, passkey)
            server.sendmail(my_email, reciver_email , message.as_string())


        return render_template("contact.html"  , Text=text , Name = name)

    else:
        text = "Contact Me"
        return render_template("contact.html" , Text = text)

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

@app.route("/form-entry" , methods=['GET', 'POST'])
def recive_data():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        text = "Yor Message sent successfully"
        
        
    
    # GET method just renders the form
    return render_template("contact.html", Name = name , Text = text  )

if __name__ == "__main__":
    app.run(port=5000, debug=True)
   