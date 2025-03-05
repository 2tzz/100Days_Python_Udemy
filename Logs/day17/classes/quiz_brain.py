class QuizBrain :


    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.score2 = 0

    
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False) :") 
        self.check_answer(user_input , current_question.answer )
        

    def still_has_question(self):
       
        if  len(self.question_list) > self.question_number  :
           
           return True
        
        else :

            return False  

    def check_answer (self , user_input , correct_answer):
        self.score2 += 1
        if user_input == correct_answer :
            self.score += 1
            print (f"correct  ✔️        Your score : {self.score}/{self.score2} ")
            

        else :
            print(f"Wrong answer ✖️         Your score :{self.score}/{self.score2}")
        
        print("\n")

    def final_score (self) :
        print(f"You've completed the challenge \n Your Finals Score Was {self.score}/{self.score2}")
