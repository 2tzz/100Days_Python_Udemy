class QuizBrain :


    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list

    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {current_question.text} (True/False) :")
        

    def still_has_question(self):
        self.question_number += 1

        
        
       

