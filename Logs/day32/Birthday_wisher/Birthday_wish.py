import smtplib
import datetime as dt
import random
import pandas


PLACEHOLDER = "[name]"

my_email = "tthiyura1@gmail.com"
passkey = "mbcn rpjl jbpq mjvc"

# with smtplib.SMTP("smtp.gmail.com") as connection :
#         connection.starttls()  #transport layer security
#         connection.login(user=my_email ,password=passkey)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs="tthiyura@gmail.com.com",
#             msg=f"Subject:monday motivation\n\n.{random.choice(quotes)}")    

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


data = pandas.read_csv("birthdays.csv")
details = data.to_dict(orient='records')

print(details)


