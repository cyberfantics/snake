import turtle as t
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self): 
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self): 
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
            turtle = t.Turtle('square')
            turtle.penup()
            turtle.color('white')
            turtle.goto(position)
            self.snake.append(turtle)
    
    def grow(self):
            self.add_segment(self.snake[-1].position())


    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x,y=new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)    
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.snake[0].setheading(LEFT)
        
    