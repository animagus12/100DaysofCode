from turtle import Screen, Turtle, color, colormode
from random import randint

tim = Turtle()
colormode(255)

for sides in range(3, 11):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for j in range(sides): 
        tim.forward(100)
        tim.left(360//sides)

screen = Screen()
screen.exitonclick()