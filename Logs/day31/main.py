from tkinter import *
from pandas  import *
import random


BACKGROUND_COLOR = "#B1DDC6"
Is_running = TRUE
current_card = {}

try :
    data = read_csv(r"data/words_to_learn.csv") 

except:
    data = read_csv(r"data/french_words.csv") 
finally:

    to_learn =  data.to_dict(orient='records')

def create_flashcard() :

    next_flashcard ()

    save_flashcard()


def save_flashcard (): 
    to_learn.remove(current_card)
    words_to_learn = DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)

def next_flashcard ():
    global current_card , flip_timer
  


    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text , text="French" , fill="Black")
    canvas.itemconfig(word_text , text=current_card["French"] , fill="Black")
    canvas.itemconfig(card_background , image=card_front_image)
    flip_timer = window.after(3000 , flip_card )




def flip_card() :

    canvas.itemconfig(title_text, text="Englsih",fill="white" )
    canvas.itemconfig(word_text, text=current_card["English"] ,fill="white") 
    canvas.itemconfig(card_background, image=card_back_image)


    green_background = PhotoImage(file=r"images/card_back.png")

    canvas_image = canvas.create_image(400, 270, image=green_background)
    #To change the image:
    canvas.itemconfig(canvas_image, image=green_background)

    
    



window = Tk()
window.title("flashy")
window.config(padx=20, pady=20 , bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800 , height= 550 , bg=BACKGROUND_COLOR, highlightthickness=0  )


card_front_image = PhotoImage(file=r"images/card_front.png")

card_back_image = PhotoImage(file=r"images/card_back.png")

card_background = canvas.create_image(400, 270 , image=card_front_image )

word_text = canvas.create_text(400 , 270 , text='Word' , fill="Black" , font=("Ariel",60,"bold"))

title_text = canvas.create_text(400 , 155 , text='French' , fill="Black" , font=("Ariel",40,"italic"))

canvas.grid(column=0 , row=0, columnspan=2 ,padx=50 , pady=50 ) 


wrong_image = PhotoImage(file=r"images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=1 , border=0 , command=next_flashcard)
wrong_button.grid(column=0,row=1)


correct_image = PhotoImage(file=r"images/right.png")
correct_button = Button(image=correct_image, highlightthickness=1 , border=0 , command=create_flashcard)
correct_button.grid(column=1,row=1)



create_flashcard()

window.mainloop()
