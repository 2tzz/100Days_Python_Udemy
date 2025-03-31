from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface :

    def __init__(self , quizz_brain :QuizBrain):
        

        self.quiz = quizz_brain
        self.window = Tk ()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20 , bg=THEME_COLOR)

        self.score_text = Label(text="score : 0",  font=("Arial",10,"bold") , background=THEME_COLOR , foreground="White" )
        self.score_text.grid(column=1 , row=0 ,pady=1)

        self.canvas = Canvas(width=300 , height= 250 , bg="white", highlightthickness=0  )
        self.question_text = self.canvas.create_text(150 , 125 , text='text' , fill="Black" , font=("Ariel",18,"italic") , width=280 )
        self.canvas.grid(column=0 , row=1, columnspan=2 , pady=50 ,padx=10 ) 


        wrong_image = PhotoImage(file=r"images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=1 , border=0 , command=self.false_pressed )
        self.wrong_button.grid(column=0,row=2)


        correct_image = PhotoImage(file=r"images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=1 , border=0 , command=self.true_pressed )
        self.correct_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question (self) :
        self.canvas.config(bg="white")
        self.score_text.config(text=f"Score : {self.quiz.score}")
        try : 
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text=q_text)
        except :
            self.canvas.itemconfig(self.question_text , text="you reached the end")
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")


    def true_pressed(self):
       is_right = self.quiz.check_answer("True")
       self.give_feedback(is_right)

    def false_pressed(self):
       is_right =  self.quiz.check_answer("False")
       self.give_feedback(is_right)

    def give_feedback(self , is_right) :
        if is_right :
           self.canvas.config(bg = "green")
        else :
           self.canvas.config(bg = "red")
        self.window.after(1000,self.get_next_question)
    
    
