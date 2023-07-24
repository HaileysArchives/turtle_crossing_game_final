from turtle import Turtle 

MOVE_DISTACNE = 10
FINISH_LINE_Y = 275
STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTACNE)

    def go_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTACNE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
