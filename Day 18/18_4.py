from turtle import Screen, Turtle, color, colormode
from random import choice, randint

tim = Turtle()
tim.speed(10)
tim.pensize(5)
colormode(255)

directions = [0, 90, 180, 270, 0, 90, 180, 270]
for _ in range(200):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.setheading(choice(directions))
    tim.fd(10)

screen = Screen()
screen.exitonclick()