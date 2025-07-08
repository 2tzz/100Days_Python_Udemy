from flask import Flask, render_template , request
import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp.gmail.com"
my_email = "tooteedemon@gmail.com"
reciver_email = 'tthiyura1@gmail.com'
passkey = "ybto bhrb bdqr mgzo"


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", active_page='home')

@app.route('/services')
def services_page():
    return render_template("services.html", active_page='services')

@app.route('/resume')
def resume_page():
    return render_template("resume.html", active_page='resume')

@app.route('/portfolio')
def portfolio_page():
    return render_template("portfolio.html", active_page='portfolio')

@app.route('/contact' , methods=['GET', 'POST'])
def contact_page():     
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message_text = request.form['message']
        text = "-- Your Message sent successfully  --"
        mail_sub = f'Thiyura you have messge from {name}'

        email_message = f"""\
        You have a message from {name} !

        {subject}

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
            return render_template("contacts.html"  , active_page='contact' , Text=text , Spantext = name)
        
    else:
        text = "Contact"
        spantext = "Me"
        return render_template("contacts.html", active_page='contact' , Text= text , Spantext = spantext)
    







if __name__ == "__main__":
    app.run(port=5000, debug=True)
   