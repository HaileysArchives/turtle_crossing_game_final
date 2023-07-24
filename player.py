from turtle import Turtle 

MOVE_DISTACNE = 5

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTACNE)