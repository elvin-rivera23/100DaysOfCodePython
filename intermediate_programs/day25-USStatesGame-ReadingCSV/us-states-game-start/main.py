# Elvin Rivera
# 8/10/2021

import pandas
import turtle

# initialize screen object
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # same directory or also "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()       # same as data["state"], gets the state attribute

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    #
    # turtle.onscreenclick(get_mouse_click_coor)      # calls function to print x, y
    # turtle.mainloop()       # keep screen open

    # this does a better job of the commented out code above

    # If answer_state is one of the states in all the states of the 50_states.csv
        # if they got it right:
            # create a turtle to write the name of the state at the state's x,y coordinate
    if answer_state == "Exit":
        # ---- LIST COMPREHENSION ----
        missing_states = [state for state in all_states if (state not in guessed_states)]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # ---- CREATE THE ABOVE BLOCK USING LIST COMPREHENSION ----

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break   # end while loop prematurely

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]       # state is =  answer
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)       # t.write(state_data.state)
        #t.write


# States to learn .csv


# screen.exitonclick()
