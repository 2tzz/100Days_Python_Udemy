from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1 
        self.ht ()
        self.penup()
        

        


    def update_scoreboard(self):
        self.clear
        self.goto(-280 , 260)
        self.write(f"level : {self.level}" , align="left", font=FONT)

    def increse_level (self):
        self.level += 1

