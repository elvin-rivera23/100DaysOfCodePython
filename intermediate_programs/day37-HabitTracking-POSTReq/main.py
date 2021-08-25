# Elvin Rivera
# 8/25/21
#
# Description: Habit tracking program. Practice with API POST requests and headers
# References: https://pixe.la , https://docs.pixe.la , https://docs.python-requests.org/en/latest/api/
# More references: https://www.w3schools.com/python/python_datetime.asp


# actual website: https://pixe.la/v1/users/elvin/graphs/graph1.html

import requests     # need this to work with APIs
from datetime import datetime

TOKEN = "hjkh34h3jk4hj34h3jh4"
USERNAME = "elvin"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# once new account created, comment out below
# response = requests.post(url=pixela_endpoint, json=user_params)    # user_params is in the form of JSON (key,value)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)    # {"message":"Success.","isSuccess":true}


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2021, month=8, day=24)
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    # "quantity": "20",
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

# update pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

#delete pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)