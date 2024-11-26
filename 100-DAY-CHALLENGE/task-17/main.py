import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()

colors = [(235, 37, 113), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50), (33, 122, 186), (52, 189, 227), (173, 44, 94), (242, 219, 57), (80, 24, 74), (127, 190, 92), (250, 223, 0), (23, 169, 122), (189, 67, 41), (207, 133, 165)]
timmy.hideturtle()
timmy.penup()
timmy.color('white')
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)