import smtplib
import datetime as dt
import random

my_email = "tthiyura1@gmail.com"
passkey = "mbcn rpjl jbpq mjvc"

# #darell200209@outlook.com

with open ("Birthday_wisher/quotes.txt") as quotes_file :

    quotes = quotes_file.readlines()

    

now = dt.datetime.now()
year = now.year
month = now.month
day = now.date()


if day == 2 :
    
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()  #transport layer security
        connection.login(user=my_email ,password=passkey)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="tooteefernando@gmail.com",
            msg=f"Subject:Hello\n\n.{random.choice(quotes)}")

