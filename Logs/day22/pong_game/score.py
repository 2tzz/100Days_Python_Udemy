from turtle import Turtle

ALIGNMENT  = 'center'
FONT = ('Comic Sans', 80, 'normal')


class Score(Turtle) :

    def __init__(self):
        super().__init__()

        self.ht()
        self.pencolor("white")
        self.penup()


    def draw_score_l (self , score):  
        self.clear()
        self.color("Red")
        self.goto(-100 , 180)
        self.write(f'{score}', move=False, align= ALIGNMENT, font= FONT)
    
    def draw_score_r (self , score): 
        self.clear() 
        self.color("Blue")
        self.goto(100 , 180)
        self.write(f'{score}', move=False, align= ALIGNMENT, font= FONT)

    def game_over (self , side):
        self.goto(0,0)
        self.write(f'Game Over {side} wins', move=False, align= ALIGNMENT, font= FONT)
