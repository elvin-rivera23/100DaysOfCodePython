# References
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

import tkinter
# from tkinter import * <-- this is so you don't have to type tkinter.class() when initializing an object

# button clicked
def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=new_text)

window = tkinter.Tk()  # Tk class to initialize an object
window.title("My First GUI Program")        # shows at top bar of program
window.minsize(width=500, height=300)            # scales to be a specified size
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))     # access Label class
# my_label.pack(side="top")         # place it on screen and center
#
# my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
button.grid(column=2, row=0)

# Entry
user_input = tkinter.Entry(width=10)
# user_input.pack()
print(user_input.get())
user_input.grid(column=3, row=2)




window.mainloop()  # keeps window on screen, built into the package


# # ---- MANY POSITIONAL ARGUMENTS ----
# # * will allow you to use as many arguments for that parameter
# def add(*args):
#     for n in args:
#         print(n)
#
# # E.g. add(3, 5, 7, 8)
# # args is a tuple
