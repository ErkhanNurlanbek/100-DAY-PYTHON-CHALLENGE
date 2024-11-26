from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f'Level: {self.score}', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', font=FONT)

    def game_over(self, position1):
        self.clear()
        self.goto(position1)
        self.write(f'GAME OVER! \nFinal level: {self.score}', font=FONT)

