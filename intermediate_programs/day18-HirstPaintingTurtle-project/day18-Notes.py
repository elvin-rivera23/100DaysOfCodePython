# import turtle as t
# from turtle import Turtle, Screen
# import turtle as t
# from turtle import *
# from module import alias <- can also do alias names

import random

#####Turtle Intro######

# tim = t.Turtle()
# tim = t.Turtle()
# to change color
# t.colormode(255)

# tim.shape("turtle")
# tim.color("tomato")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)


########### Challenge 2 - Draw a Dashed Line ########

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

########### Challenge 3 - Draw Shapes ########
# need two variables sides and angle
# total_sides = 3
#
# while total_sides <= 10:
#     angle = 360/total_sides
#     for i in range(total_sides):
#         tim.forward(100)
#         tim.right(angle)
#     total_sides +=1


# # Instructor way
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for side in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range (3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)        # shape_side_n is the num of sides a shape has, starts at 3 goes up to 10




########### Challenge 4 - Random Walk ########




# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)       # <-- Tuple
#     return random_color

# for _ in range(200):
#     # tim.color(random.choice(colours))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# create new object screen
# screen = Screen()
# screen.exitonclick()

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        # current_heading = tim.heading()
        # tim.setheading((current_heading + 10))
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

########### Challenge 5 - Spirograph ########