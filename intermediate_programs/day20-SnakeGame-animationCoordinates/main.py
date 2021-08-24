# Elvin Rivera
# 8/4/2021


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# initialize other scoreboards
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# this is to move the snake, listening for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)     # creates slight lag after each segment moves
    snake.move()        # call the method from snake class to move

    # Detect collision with food, food is 10x10
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail, using SLICING (list/tuple), denoted by " : "
    # this gives us everything in the list besides the first item
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         # game_is_on = False
    #         # scoreboard.game_over()


    # ---- UPDATED VERSION DAY 24 ------
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     # if snake head is within 10 of any segment
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #     #if head collides with any segment in the tail:
    #         #trigger game_over








screen.exitonclick()