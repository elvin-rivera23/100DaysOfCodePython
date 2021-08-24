# # in the same directory, so use relative data path
# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()        # .readlines() takes each line in the file and turn it into item in a list
#     print(data)

# # built in python library
# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)       # reads file and outputs data
    # print(data)
    # temperatures = []
    # for temp in data:
        # print(row)

        # Expected output:
        # ['day', 'temp', 'condition']
        # ['Monday', '12', 'Sunny']
        # ['Tuesday', '14', 'Rain']
        # ['Wednesday', '15', 'Rain']
        # ['Thursday', '14', 'Cloudy']
        # ['Friday', '21', 'Sunny']
        # ['Saturday', '22', 'Sunny']
        # ['Sunday', '24', 'Sunny']

    # for temperature in data:
    #     # exclude column title
    #     if temperature[1] != "temp":
    #         temperatures.append(int(temperature[1]))        # turn the values into int instead of str
    #
    # print(temperatures)

# ----- REFERENCES: https://pandas.pydata.org -----

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)

# # EXPECTED OUTPUT:
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny


# print(data["temp"])

# # EXPECTED OUTPUT:

# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64


# ----- DataFrames & Series: working with Rows and Columns -----

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))       # output: <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"]))       # output: <class 'pandas.core.series.Series'>

# notes: .Series equivalent to single column list

# data_dict = data.to_dict()      # creates data dictionary, each column has its own dictionary
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)        # [12, 14, 15, 14, 21, 22, 24]
#
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
#
# average = int(total_temp/len(temp_list))
# print(average)
#
# # # instructor way
# # average = sum(temp_list) / len(temp_list)
# # print(int(average))
#
#
# # built in function for pandas
# print(data["temp"].mean())
#
# # to get the maximum value
# # note: data = pandas.read_csv("weather_data.csv")
# print(data["temp"].max())       # max is 24


# # Get data in Columns
# print(data["condition"])
# data.condition      # pandas converts each series into attributes

# # Get data in Row: table[column_search_through]
# # data.day = data["day"]
# print(data[data.day == "Monday"])
#
# # Challenge: print day that had highest temp in the week
# print(data[data.temp == data.temp.max()])       # 6  Sunday    24     Sunny


monday = data[data.day == "Monday"]
print(monday.condition)     # 0    Sunny

# convert from celsius to farenheit

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Elvin", "Diana", "Jonny"],
    "scores": [76, 56, 65]
}


data = pandas.DataFrame(data_dict)
print(data)

#   students  scores
# 0    Elvin      76
# 1    Diana      56
# 2    Jonny      65

# this will create csv in current directory
data.to_csv("new_data.csv")
