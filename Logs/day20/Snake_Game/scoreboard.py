from turtle import Turtle


class ScoreBoard(Turtle) :

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.pencolor("white")
        self.penup()
        self.goto(0 , 275)
        self.pendown()

    def show_score (self):
        
        self.clear()
        self.score += 1    
        self.write(f'Score : {self.score}', move=False, align='center', font=('Arial', 15, 'normal'))