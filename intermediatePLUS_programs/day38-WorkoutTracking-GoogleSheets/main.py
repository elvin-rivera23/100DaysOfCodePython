# Elvin Rivera
# 8/26/21
#
# Description: Workout Tracking Using Google Sheets
#
# References: https://beta.openai.com/docs/introduction/overview ,
# https://www.nutritionix.com/business/api , https://sheety.co ,
# Nutritionix API v2 Doc https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#


import os
import requests
from datetime import  datetime

API_KEY = os.environ["Nutritionix API Key"]
APP_ID = os.environ["Nutritionix App ID"]

# variables for params, based on yourself
GENDER = "male"
WEIGHT_KG = 72.5
HEIGHT_CM = 170.18
AGE = 27

# API Endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/username/projectName/sheetName"  # depends on your info

# step 2: get exercise stats with natural language queries
# reference: https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
exercise_prompt = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# need to authenticate request, so needs a header
response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()    # json format
print(result)

# format date and time: https://www.w3schools.com/python/python_datetime.asp
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# https://www.w3schools.com/python/ref_string_title.asp -> String to Title
# each exercise in the result will be put into the sheet columns
# nested dictionary
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

