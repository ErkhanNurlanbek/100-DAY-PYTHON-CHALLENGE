from turtle import Turtle, Screen

mikey = Turtle()
screen = Screen()


def move_forwards():
    mikey.forward(10)


def move_backwards():
    mikey.backward(10)


def turn_right():
    mikey.right(10)


def turn_left():
    mikey.left(10)


def clear():
    mikey.clear()
    mikey.penup()
    mikey.home()
    mikey.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
