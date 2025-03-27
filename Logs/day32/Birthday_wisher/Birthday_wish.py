import smtplib
import datetime as dt
import random
import pandas


PLACEHOLDER = "[NAME]"

my_email = "tthiyura1@gmail.com"
passkey = "mbcn rpjl jbpq mjvc"
birthday_names = []
birthday_age = []
birthday_emails = []
files = []
newletters = []
  
now = dt.datetime.now()
year = now.year
# month = now.month
current_month = 9
# day = now.day
current_day = 11


data = pandas.read_csv("birthdays.csv")
details = data.to_dict(orient='records')

##check for a birthday

for item in details :
    if item["month"] == current_month and item["day"] == current_day :
        birthday_names.append(item["name"])
        birthday_emails.append(item["email"])

    
for i in range(0 , len(birthday_names)) :

    with open(r"letter_templates/letter_1.txt") as f1, open(r"letter_templates/letter_2.txt") as f2, open(r"letter_templates/letter_3.txt") as f3:
        files = [f1 , f2 , f3]
        random_file = random.choice(files)
        email = birthday_emails[i]
        letter_contents = random_file.read()
        stripped_name = birthday_names[i].strip()
        new_letter =  letter_contents.replace(PLACEHOLDER , stripped_name)

        # print(f"loop {i}\n  listname{birthday_names[i]} \n strippedname{stripped_name}\n NEW\n{new_letter}  \n\n\n")

       #SENDING  MAILS 
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()  #transport layer security
            connection.login(user=my_email ,password=passkey)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=f"{email}",
                msg=f"Subject:Hey Its your Birthdayy\n\n{new_letter}")


    
    
        
            

        
