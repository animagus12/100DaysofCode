from turtle import Screen, Turtle, colormode
from random import choice
import colorgram

tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
colormode(255)

# Extracting colors from an image using colorgram
'''
colors = colorgram.extract('C:/Users/subhr/OneDrive/Documents/Programs/Python/#100DaysOfCode/Day 18/image.jpg', 100)

rgb_colors = []
for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''

color_list =  [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0), (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)] 

tim.penup()
tim.goto(-225, -275)
tim.pendown()

length = 50
for j in range(0, 10):
    tim.penup()
    tim.goto(-225, -275)
    tim.left(90)
    tim.forward(length)
    tim.right(90)
    tim.pendown()
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    length += 50

screen = Screen()
screen.exitonclick()