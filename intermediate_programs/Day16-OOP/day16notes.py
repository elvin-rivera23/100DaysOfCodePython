# ----- PART 1 -----

# # Reference: https://docs.python.org/3/library/turtle.html , https://cs111.wellesley.edu/labs/lab01/colors
#
#
# # import turtle
#
# # from the module call a Class (PascalCase)
# # timmy = turtle.Turtle()
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()    # this is a new object called timmy
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("goldenrod1")
# timmy.forward(100)
#
# # here's what gets printed in the console: "/Users/elvinrivera/Programming/100 Days of Code/intermediate_programs/
# # Day16-OOP/venv/bin/python" "/Users/elvinrivera/Programming/100 Days of Code/intermediate_programs/Day16-OOP/main.py"
# # <turtle.Turtle object at 0x7fde1018c9d0>
#
# # class notation: object.attribute e.g. car.speed
#
# my_screen = Screen()
# print(my_screen.canvheight) # screen is the object, canvheight is an attribute (variable)
#
# # Here is how to call a method from an object
# # e.g. car.stop()   calling the object, and then calling the function (Method) associated to that object
# # functions tied to an object are called a method
#
# my_screen.exitonclick()


# ----- PART 2 ------
# References: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

# import prettytable  # to access, right click prettytable, go to, implementation

from prettytable import PrettyTable

table = PrettyTable()   # new object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)
