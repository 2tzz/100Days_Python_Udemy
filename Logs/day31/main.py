from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"




window = Tk()
window.title("flashy")
window.config(padx=20, pady=20 , bg=BACKGROUND_COLOR)

canvas = Canvas(width=800 , height= 550 , bg=BACKGROUND_COLOR, highlightthickness=0  )


white_background = PhotoImage(file=r"images\card_front.png")
canvas.create_image(400, 270 , image=white_background )

word_text = canvas.create_text(400 , 270 , text='trouve' , fill="Black" , font=("Ariel",60,"bold"))

title_text = canvas.create_text(400 , 155 , text='Title' , fill="Black" , font=("Ariel",40,"italic"))

canvas.grid(column=0 , row=0, columnspan=2 ,padx=50 , pady=50 ) 

wrong_image = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0 , border=0)
wrong_button.grid(column=0,row=1)


correct_image = PhotoImage(file=r"images\right.png")
correct_button = Button(image=correct_image, highlightthickness=0 , border=0)
correct_button.grid(column=1,row=1)







































window.mainloop()
