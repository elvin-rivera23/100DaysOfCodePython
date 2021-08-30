import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "SHEETY PRICES ENDPOINT URL"
SHEET_USERS_ENDPOINT = "SHEETY USERS ENDPOINT"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}  # destination data is dictionary format

    def get_destination_data(self):
        # 2. use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]  # destination data from json, prices is key
        # 3. Try importing pretty print and printing the data out again using pprint().
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            # update destination by creating new dict, price is key, value is dictionary of iataCodes
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
