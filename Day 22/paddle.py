from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, loc):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.turtlesize(stretch_wid=None, stretch_len=5)
        self.penup()
        self.goto(loc)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
