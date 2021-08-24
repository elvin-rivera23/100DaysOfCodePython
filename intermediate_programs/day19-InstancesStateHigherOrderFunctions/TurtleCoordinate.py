# Elvin Rivera
# 8/3/2021
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

# range function starts at 0 and doesnt include end number
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])       #use the turtle index to get index of y_positions
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)      # or all_turtles.append(new_turtle)

# If there is a user bet then race is going to start
if user_bet:
    is_race_on = True

# while statement is still True do these things
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:     # 250 - (40/2) = 230
            is_race_on = False      # stop once a turtle reaches 230 and process the next if statement
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()