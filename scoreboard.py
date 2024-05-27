from turtle import Turtle as t
ALLIGN = 'left'
FONT = ('Arial',24,'bold')
POSITION = (-50,215)
class ScoreBoard(t):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(POSITION)
        self.score = 0
        self.updatedScore()

    def updatedScore(self):
        self.write(f'Score: {self.score}',align=ALLIGN,font=FONT)
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.updatedScore()

    def gameOver(self):
        self.goto(-60,0)
        self.write('GameOver',align=ALLIGN,font=FONT)