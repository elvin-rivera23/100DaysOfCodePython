# Elvin Rivera
# 8/22/21
# Description: check if it's raining, practice sending SMS with Twilio API


# References: https://openweathermap.org/current , https://openweathermap.org/api/one-call-api ,
# https://home.openweathermap.org/users/sign_in , https://www.latlong.net , http://jsonviewer.stack.hu

# More References: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2 , https://www.ventusky.com ,
# https://www.w3schools.com/python/ref_func_slice.asp ,
# https://stackoverflow.com/questions/509211/understanding-slice-notation

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "API KEY"  # api.openweathermap.org/data/2.5/weather?q=Fresno,US#appid=36478164197364e82910 <- ending is key
account_sid = "SID from Twilio account"
auth_token = "Token from Twilio"

# parameters are in dictionary form
weather_params = {
    "lat": 34.052235,
    "lon": -118.243683,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)    # 200 is successful
response.raise_for_status()
weather_data = response.json()  # get data in json format
weather_slice = weather_data["hourly"][:12]  # goes to 11, whatever number -1

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]  # STARTS AS LIST, GOES TO DICTIONARY
    if int(condition_code) < 700:
        will_rain = True

# Reference: https://www.twilio.com/docs/sms/quickstart/python
if will_rain:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+15017122661',
        to='+TwilioNumberUsedToSignUp'
    )
    print(message.status)

# print(weather_data["hourly"][0]["weather"][0])
