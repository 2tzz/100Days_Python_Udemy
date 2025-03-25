from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"




window = Tk()
window.title("flashy")
window.config(padx=20, pady=20 , bg=BACKGROUND_COLOR)

canvas = Canvas(width=800 , height= 526 , bg=BACKGROUND_COLOR, highlightthickness=0)
white_background = PhotoImage(file=r"images\card_front.png")
canvas.create_image(400, 200 , image=white_background )
timer_text = canvas.create_text(400 , 150 , text='trouve' , fill="Black" , font=("Ariel",35,"bold"))
canvas.grid(column=0 , row=0,columnspan=2 ) 










































window.mainloop()
