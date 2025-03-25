from tkinter import *
from pandas  import *
import random


BACKGROUND_COLOR = "#B1DDC6"
Is_running = TRUE
current_card = {}

data = read_csv(r"data/french_words.csv") 
to_learn =  data.to_dict(orient='records')

def create_flashcard() :

    global current_card
    
    current_card = random.choice(to_learn)

    print(current_card)

    canvas.itemconfig(title_text , text="French")
    canvas.itemconfig(word_text , text=current_card["French"])


def flip_card() :

    canvas.itemconfig(title_text, text="Englsih")
    canvas.itemconfig(word_text, text=current_card["English"]) 


    green_background = PhotoImage(file=r"images\card_back.png")

    canvas_image = canvas.create_image(400, 270, image=green_background)
    #To change the image:
    canvas.itemconfig(canvas_image, image=green_background)

    
    



window = Tk()
window.title("flashy")
window.config(padx=20, pady=20 , bg=BACKGROUND_COLOR)


window.after(3000, func=flip_card)


canvas = Canvas(width=800 , height= 550 , bg=BACKGROUND_COLOR, highlightthickness=0  )


white_background = PhotoImage(file=r"images\card_front.png")
canvas.create_image(400, 270 , image=white_background )

word_text = canvas.create_text(400 , 270 , text='Word' , fill="Black" , font=("Ariel",60,"bold"))

title_text = canvas.create_text(400 , 155 , text='French' , fill="Black" , font=("Ariel",40,"italic"))

canvas.grid(column=0 , row=0, columnspan=2 ,padx=50 , pady=50 ) 


wrong_image = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=1 , border=0 , command=create_flashcard )
wrong_button.grid(column=0,row=1)


correct_image = PhotoImage(file=r"images\right.png")
correct_button = Button(image=correct_image, highlightthickness=1 , border=0 , command=create_flashcard)
correct_button.grid(column=1,row=1)



create_flashcard()

window.mainloop()
