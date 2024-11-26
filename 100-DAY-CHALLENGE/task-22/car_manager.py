import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list =[]


    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 3:
            porsche = Turtle('square')

            porsche.penup()
            porsche.shapesize(stretch_wid=1, stretch_len=2)
            porsche.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            porsche.goto(270, random_y)
            self.car_list.append(porsche)

    def move(self, speed):
        for car in self.car_list:
            car.backward(speed)

