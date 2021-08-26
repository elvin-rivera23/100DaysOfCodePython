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

# hide env variables: https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values
# https://docs.replit.com/archive/secret-keys#:~:text=env%20files%20are%20used%20for,see%20the%20contents%20of%20the%20.
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

# ---- STEP 4: AUTHENTICATION TYPES ----

# #  -- no authentication --
# sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)

# # -- basic Authentication--
# # reference: https://docs.python-requests.org/en/master/user/authentication/#basic-authentication
# sheet_response = requests.post(
#     url=sheety_endpoint,
#     json=sheet_inputs,
#     auth=(
#         os.environ["USERNAME"],
#         os.environ["PASSWORD"],
#     )
# )

# --- bearer Token ---
# reference: https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

sheet_response = requests.post(
    url=sheety_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)