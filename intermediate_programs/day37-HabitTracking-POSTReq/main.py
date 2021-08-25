# Elvin Rivera
# 8/25/21
#
# Description: Habit tracking program. Practice with API POST requests and headers
# References: https://pixe.la , https://docs.pixe.la , https://docs.python-requests.org/en/latest/api/

# actual website: https://pixe.la/v1/users/elvin/graphs/graph1.html

import requests     # need this to work with APIs

TOKEN = "hjkh34h3jk4hj34h3jh4"
USERNAME = "elvin"

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
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)    # {"message":"Success.","isSuccess":true}