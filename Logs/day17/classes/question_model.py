class Question :

    def __init__(self , question ,correct_answer):
        
        self.text = question
        self.answer = correct_answer

    
class QuestioonA(Question):
    def __init__(self, question, correct_answer):
        super().__init__(question, correct_answer)
    

