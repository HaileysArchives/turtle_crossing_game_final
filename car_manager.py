from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
X = 300
STARTING_POSITIONS = [(X, -225), (X, -200), (X, -175), (X, -150), (X, -125), (X, -100), (X, -75), (X, -50), (X, -25),
                      (X, 0), (X, 25), (X, 50), (X, 75), (X, 100), (X, 125), (X, 150), (X, 175), (X, 200), (X, 225)]


class CarManager:
    def __init__(self):
        self.cars = []
        self.MOVE_INCREMENT = 0

    def move(self):
        for car in self.cars:
            if car.xcor() > -330:
                car.backward(STARTING_MOVE_DISTANCE + self.MOVE_INCREMENT)
            else:
                self.cars.remove(car)

    def make_cars(self):
        car = Turtle('square')
        car.penup()
        car.color(random.choice(COLORS))
        car.turtlesize(1.0, 2.0)
        car.setposition(random.choice(STARTING_POSITIONS))
        self.cars.append(car)

    def increase_car_speed(self):
        self.MOVE_INCREMENT += 10
