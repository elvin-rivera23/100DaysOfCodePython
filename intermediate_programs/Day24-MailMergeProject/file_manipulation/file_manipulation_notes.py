# file = open("my_file.txt")

# with, automatically knows to open and close it once we're done with it
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# file.close()        # once python opens file, it takes resources. Need to close it.

# default set to read-only, change mode to be able to write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# if you want to append to a file, change mode to  "a"
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# NOTE: If you try to open a file in write mode and it doesn't exist, it will create it for you from scratch
with open("new_file.txt", mode="w") as file:
    file.write("New text.")


# # Example with absolute file path
# with open("/Users/elvinrivera/desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# Example for relative file path, working from elvinrivera
# ../ <-- goes up one file path from working directory
with open("../../Desktop/new_file.txt") as file:
    file.write("New text.")