import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

score_board = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collison with car

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect crossing
    if player.at_finish():
        score_board.update_scoreboard()
        player.start_pos()
        car_manager.speed_increase()

screen.exitonclick()
