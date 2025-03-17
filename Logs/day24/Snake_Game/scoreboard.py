from turtle import Turtle
import random

ALIGNMENT  = 'center'
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle) :

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.ht()
        self.pencolor("white")
        self.penup()
        

    def draw_boundry(self):
        self.pencolor(self.random_color())
        self.pensize(4)
        self.penup()
        self.goto(-284,264)
        self.pendown()
        self.goto(284,264)
        self.goto(284, -284)
        self.goto(-284,-284)
        self.goto(-284,264)
        self.penup()

    def show_score (self):
        
        self.goto(0 , 275)
        self.pendown()
        self.clear()  
        self.write(f'Score : {self.score}   High Score : {self.high_score}'   , move=False, align= ALIGNMENT, font= FONT)

    def increse_score(self):
        self.score += 1
        self.show_score()

    def reset(self) :

        if self.score > self .high_score :

            self.high_score = self.score
      
        self.score = 0

    # def game_over(self):

    #     self.goto(0 , 0)
    #     self.write(f'GAME OVER', move=False, align= ALIGNMENT, font= FONT)

    def random_color(self):
        r = random.randint(0, 255) / 255.0  # Normalize RGB values to [0, 1]
        g = random.randint(0, 255) / 255.0
        b = random.randint(0, 255) / 255.0
        color_tuple = (r, g, b)  # Return normalized RGB tuple
        return color_tuple