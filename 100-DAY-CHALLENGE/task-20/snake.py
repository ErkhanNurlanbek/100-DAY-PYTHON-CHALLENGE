from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for turtle in STARTING_POS:
            self.add_turtle(turtle)

    def add_turtle(self, turtle):
        mikey = Turtle(shape='square')
        mikey.penup()
        mikey.color('white')
        mikey.goto(turtle)
        self.all_turtles.append(mikey)

    def extend(self):
        self.add_turtle(self.all_turtles[-1].position())

    def move(self):
        for turtle in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle - 1].xcor()
            new_y = self.all_turtles[turtle - 1].ycor()
            self.all_turtles[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

