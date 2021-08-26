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