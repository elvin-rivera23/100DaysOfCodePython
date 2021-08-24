# PyDev console: starting.
# Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53)
# [Clang 6.0 (clang-600.0.57)] on darwin
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# name = "Elvin"
# new_list = [letter for letter in name]
# range_list = [number*2 for number in range(1,5)]


# list comprehension with Range function
even_number = [number*2 for number in range(1,5)]
print(even_number)

names = ["Elvin", "Diana", "Rampage", "Mason", "Jonny", "Bryan"]


# list comprehension with a condition
long_names = [name for name in names if len(name) > 5]

short_names = [name.upper() for name in names if len(name) <= 5]




# ---- DICTIONARY COMPREHENSION ----
import random

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
name = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1,100) for student in name}


# passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in students_scores.items()
                   if score >= 50}       # .items gets all items in dict



