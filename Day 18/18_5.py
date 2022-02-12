from turtle import Screen, Turtle, color, colormode
from random import randint

tim = Turtle()
tim.speed('fastest')
colormode(255)

gap = 2

for _ in range(360 // gap):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.circle(100)
    tim.left(gap)

screen = Screen()
screen.exitonclick()