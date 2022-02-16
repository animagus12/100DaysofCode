from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = ScoreBoard()

# if right_paddle.position().ycor != -400 or right_paddle.position().ycor != 400:
screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

right_point = 0
left_point = 0
game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection of collison with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # Detection of collison with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect when Right Paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when Left Paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
