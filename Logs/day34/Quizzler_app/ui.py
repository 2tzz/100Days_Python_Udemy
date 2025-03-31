from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface :

    def __init__(self):
        
        self.window = Tk ()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20 , bg=THEME_COLOR)

        score_text = Label(text="score :",  font=("Arial",8,"bold") , background=THEME_COLOR , highlightcolor="white" )
        score_text.grid(column=1 , row=0 ,pady=1)

        canvas = Canvas(width=400 , height= 600 , bg="white", highlightthickness=0  )
        question_text = canvas.create_text(100 , 100 , text='text' , fill="Black" , font=("Ariel",20,"italic"))
        canvas.grid(column=0 , row=1, columnspan=2 ,padx=50 , pady=50 ) 


        wrong_image = PhotoImage(file=r"images/false.png")
        wrong_button = Button(image=wrong_image, highlightthickness=1 , border=0 )
        wrong_button.grid(column=0,row=2)


        correct_image = PhotoImage(file=r"images/true.png")
        correct_button = Button(image=correct_image, highlightthickness=1 , border=0 )
        correct_button.grid(column=1,row=2)



        self.window.mainloop()

