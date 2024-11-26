from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
guess = screen.textinput('Bets', 'Which turtle will win? Enter a color:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [70, 40, 10, -20, -50, -80]
all_turtles = []

for turtle in range(0, 6):
    n_turtle = Turtle(shape='turtle')
    n_turtle.penup()
    n_turtle.color(colors[turtle])
    n_turtle.goto(-230, y_position[turtle])
    all_turtles.append(n_turtle)

if guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 235:
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f'You win, {winning_color} has won!')
            else:
                print(f'You lose, {winning_color} has won!')
            is_race_on = False

        r_dist = random.randint(0, 10)
        turtle.forward(r_dist)



screen.exitonclick()