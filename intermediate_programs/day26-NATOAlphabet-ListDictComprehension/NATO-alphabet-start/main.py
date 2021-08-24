# Elvin Rivera
# 8/11/2021


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())       # take the df and turn it into dictionary, without to_dict, it looks like a csv format

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# .letter, .code -> columns in csv
# iterrows, goes through each row of the dictionary, for each index and row
# {"A": "Alfa", "B": "Bravo"} -> row.A: row.Alfa
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}       # dictionary comprehension
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

# List comprehension, but the word is what we're iterating through 
# letter will be the value for each key in the phonetic dictionary. E.g. E : Echo, L : Lima, etc.
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)