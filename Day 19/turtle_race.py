from turtle import Turtle, Screen, color, shape
import turtle
from random import randint

screen  = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will rin the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_loc = -90
all_turtles = []

for i in range(7):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_loc)
    y_loc += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} is the winner!")
        dist = randint(0, 10)
        turtle.forward(dist)


screen.exitonclick()