from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen() 
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.make_cars()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 21:
            scoreboard.game_over()
            game_is_on = False

    if player.finish_line():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.update_score()

screen.exitonclick()
