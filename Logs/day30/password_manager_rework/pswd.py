from tkinter import *
from tkinter import messagebox
import math
from random import choice , randint , shuffle
import pyperclip
import json


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Hobo Std"

# #updating old data with new data
#                 data.update(new_data)

# ---------------------------- search ------------------------------- #

def search_web():

    website = web_entry_getx.get()
     
    with open("passwords.jason" , mode = "r") as file:
         #reading old data
        data = json.load(file)

    for dic in data :
        if website == dic :
            returnemail = data[dic]["email"]
            returnpassword = data[dic]["password"]

    email_entry.delete(0,'end')   
    password_entry.delete(0,'end') 
    password_entry.insert(0 , returnpassword)
    email_entry.insert(0 , returnemail)

         
                
   
                
        

   






# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#from password gen project
def gen_password():

    password_entry.delete(0,'end') 

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_list = []

    letter_list = [choice(letters) for char in range(randint(8,10)) ]
    symbol_list = [choice(numbers) for char in range(randint(2,4)) ]
    number_list = [choice(symbols) for char in range(randint(2,4)) ]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
        password
        
    pyperclip.copy(password)
    password_entry.insert(0 , password)
        

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_user_data() :

    website = web_entry_getx.get()
    email = email_entry_getx.get()
    password_ = password_entry_getx.get()

    new_data = {
        website : {
            "email" : email,
            "password" : password_,
        }
    }

    if len(website) < 2 or len(password_) < 2 :

        messagebox.showinfo(title="check the fields" , message="Your webiste data or password is too short !")

    else :
        try:
            with open("passwords.jason" , mode = "r") as file:
                #reading old data
                data = json.load(file)
                #updating old data with new data
                data.update(new_data)
        except:
            with open("passwords.jason" , mode = "w") as file:  

                json.dump(new_data , file  , indent=4)
            
        else:
            with open("passwords.jason" , mode = "w") as file:   
                #new updated data
                json.dump(data , file  , indent=4)
        finally:
            web_entry.delete(0,'end')   
            password_entry.delete(0,'end')





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")

window.config(padx=20, pady=20 )

web_entry_getx = StringVar()
email_entry_getx = StringVar()
password_entry_getx = StringVar()


canvas = Canvas(width=200 , height= 200 , highlightthickness=0  )
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image=tomato_image  )
canvas.grid(column=1 , row=0 ) 

website = Label(text="Website :",  font=(FONT_NAME,8,"bold"))
website.grid(column=0 , row=1 ,pady=1)

web_entry = Entry(width=31 , border=1 , background='#e6f3ff' , textvariable=web_entry_getx)
web_entry.focus()
web_entry.grid(column=1 , row=1 ,columnspan=1 ,pady=1)

search_button = Button(text="search",font=(FONT_NAME,8,"bold"), height=1 ,width=16 , command=search_web , bg='#d1eaff' ,borderwidth=1 )
search_button.grid(column=2 , row=1 ,pady=1 , padx=3)

email = Label(text="Email / User_Name :",  font=(FONT_NAME,8,"bold"))
email.grid(column=0 , row=2 ,pady=1)

email_entry = Entry(width=52 , border=1 , background='#e6f3ff' ,textvariable=email_entry_getx)
email_entry.insert(0 , "tthiyura1@gmail.com")
email_entry.grid(column=1 , row=2 ,columnspan=2)


password = Label(text="Password :",  font=(FONT_NAME,8,"bold"))
password.grid(column=0 , row=3 )

password_button = Button(text="Generete Password",font=(FONT_NAME,8,"bold"), height=1 ,width=16 , command=gen_password , bg='#d1eaff' ,borderwidth=1 )
password_button.grid(column=2 , row=3 ,pady=1 , padx=3)

password_entry = Entry(width=31 , border=1 , background='#e6f3ff' , textvariable=password_entry_getx)
password_entry.grid(column=1 , row=3 )



add_button = Button(text="Add",font=(FONT_NAME,9,"bold") ,width=44, height=1  , command=save_user_data , bg='#d1eaff', borderwidth=1  )
add_button.grid(column=1 , row=4 , columnspan=2 ,pady=1)








window.mainloop()