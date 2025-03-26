import smtplib

my_email = "tthiyura1@gmail.com"
passkey = "mbcn rpjl jbpq mjvc"

with smtplib.SMTP("smtp.gmail.com") as connection :
    connection.starttls()  #transport layer security
    connection.login(user=my_email ,password=passkey)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="darell200209@outlook.com",
        msg="Subject:Hello\n\nThis is the body of my email.")
    

