import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
#SET SCREEN
s = t.Screen()
s.tracer(0)
s.title('My Snake Game')
s.bgcolor('black')
s.setup(width=500,height=500)
#CREATE NEW SNAKE
snake = Snake()
isgameon = True
#CONTROL MOVEMENT OF SNAKE
s.listen()
s.onkey(snake.down,'Down')
s.onkey(snake.right,'Right')
s.onkey(snake.up,'Up')
s.onkey(snake.left,'Left')
#create food on screen
food = Food()
#create scoreboard on screen
score = ScoreBoard()
#MAIN PART OF THE GAME
while isgameon:
    s.update()
    time.sleep(0.5)
    snake.move()
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        score.gameOver()
        isgameon = False
    elif snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.grow()
    else:
        for segment in snake.snake[1:]:
            if snake.head.distance(segment)<10:
                score.gameOver()
                isgameon = False
s.exitonclick()