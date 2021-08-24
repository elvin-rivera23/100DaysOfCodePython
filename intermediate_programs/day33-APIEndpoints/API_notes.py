# Reference HTTP Status Codes: https://httpstatuses.com
# https://www.latlong.net/Show-Latitude-Longitude.html

import requests
from datetime import datetime

MY_LAT = 36.7783
MY_LONG = 119.4179

# # response = requests.get(url="http://api.open-notify.org/is-now.json")
# # print(response.status_code)     # 404
#
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)     # 200
# # if response.status_code == 404:
# #     raise Exception("The resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data.")
#
# response.raise_for_status()
#
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]       # how to get value of key that's in a key
# print(longitude)
# latitude = data["iss_position"]["latitude"]
# print(latitude)
#
# iss_position = (longitude, latitude)
# print(iss_position)



# ----- API PARAMETERS ------

# https://sunrise-sunset.org/api , https://www.w3schools.com/python/ref_string_split.asp

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
# print(sunrise.split("T")[1].split(":")[0])


time_now = datetime.now()
print(time_now.hour)