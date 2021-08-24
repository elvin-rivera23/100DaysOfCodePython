# NOTE: with open("file.name") as temp_variable


with open("file1.txt") as file1:
    file_1_data = file1.readlines()     # reads the data and creates a list (line by line)

with open("file2.txt") as file2:
    file_2_data = file2.readlines()     # reads the data and creates a list (line by line)


# result = [new_item for item in list if test]
result = [int(num) for num in file_1_data if num in file_2_data]


# Write your code above 👆

print(result)

