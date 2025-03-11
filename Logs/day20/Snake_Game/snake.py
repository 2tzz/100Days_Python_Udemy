from turtle import Turtle

STARTING_POSITIONS = [(0,0) , (-2,0) ,(-4,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    

    def __init__(self):

        self.segments  = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):

        for positions in  STARTING_POSITIONS:

            new_segment = Turtle(shape="square")
            new_segment.color("White")
            new_segment.shapesize(0.5,0.5)
            new_segment.penup()
            new_segment.goto(positions)
            self.segments.append(new_segment)

        



    def move(self) :

        for  seg_num in range (len(self.segments) - 1, 0 , -1) :
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)

    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(MOVE_DISTANCE)
            

    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DISTANCE)
            

    def left (self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(MOVE_DISTANCE)
            

    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(MOVE_DISTANCE)
            
        

