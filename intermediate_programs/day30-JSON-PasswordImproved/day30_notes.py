# # with open("a_file.txt") as file:
# #     file.read()
#
# # File Not Found Error
# try:
#     file = open("a_file.txt")   # failed
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["adsdf"])    # fails and creates exception
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that I made up.")
#
# # Raise own exceptions

# raise own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)