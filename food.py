from turtle import Turtle as t
import random as r
class Food(t):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('green')
        self.speed(0)
        self.refresh()

    def refresh(self):
        x_value = r.randint(-230,230)
        y_value = r.randint(-230,230)
        self.goto(x=x_value,y=y_value)
    