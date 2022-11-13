from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

    def win(self):
        self.write('YOU WIN', align='center', font=('Courier', 88, 'normal'))

    def lose(self):
        self.write('YOU LOSE', align='center', font=('Courier', 88, 'normal'))

