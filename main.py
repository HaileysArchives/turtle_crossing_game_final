from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
import time

screen = Screen() 
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

car_manager = CarManager()
player = Player()

# screen.listen()
# screen.onkey(player.go_up, "Up")
# screen.onkey(player.go_left, "Left")
# screen.onkey(player.go_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.make_cars()
    car_manager.move()
    player.move()


screen.exitonclick()
