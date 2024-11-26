from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'Game Over!', move=False, align=ALIGNMENT, font=FONT)


    def point(self):
        self.score += 1
        self.clear()
        self.update_score()
