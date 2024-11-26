import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, MOVE_DISTANCE
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard((-280, 250))

screen.listen()
screen.onkey(player.move, 'w')

car_speed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move(car_speed)

    for car in car_manager.car_list:
        if car.distance(player) < 17:
            scoreboard.game_over((-280, 200))
            game_is_on = False

    if player.ycor() == FINISH_LINE_Y:
        player.new_lvl()
        scoreboard.increase_score()
        for car in car_manager.car_list:
            car_speed += 0.05



screen.exitonclick()
