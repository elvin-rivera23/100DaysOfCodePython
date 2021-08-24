# Higher Order Functions & Even Listeners

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# def move_backwards()
#     tim

screen.listen()
screen.onkey(key="space", fun=move_forwards())
