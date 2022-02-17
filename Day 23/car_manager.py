from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move()
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 4) == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, randint(-240, 240))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.carspeed)

    def speed_increase(self):
        self.carspeed += MOVE_INCREMENT
