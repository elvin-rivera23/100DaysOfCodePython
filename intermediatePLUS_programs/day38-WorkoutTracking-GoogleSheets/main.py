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

API_KEY = os.environ["Nutritionix API Key"]
APP_ID = os.environ["Nutritionix App ID"]

# variables for params, based on yourself
GENDER = "male"
WEIGHT_KG = 72.5
HEIGHT_CM = 170.18
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# step 2: get exercise stats with natural language queries
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