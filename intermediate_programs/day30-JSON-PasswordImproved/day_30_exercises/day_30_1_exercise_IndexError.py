fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")




make_pie(4)

# NOTE: will search index 4, try to see if it's there. It's not so go to the exception: print("Fruit pie")
