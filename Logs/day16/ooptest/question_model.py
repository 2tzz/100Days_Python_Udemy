from data import question_data

class Question:
    def __init__(self , q_text , q_answer):
        self.question = q_text
        self.answer = q_answer



    def still_has  (self) :
        if self.answer == "True" :
            print("you are correct")
        else:
            print("you are wrong")