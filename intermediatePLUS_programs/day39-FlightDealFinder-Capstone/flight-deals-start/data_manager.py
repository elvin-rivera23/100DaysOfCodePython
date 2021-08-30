import requests

SHEETY_PRICES_ENDPOINT = "SHEETY PRICES ENDPOINT URL"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}      # destination data is dictionary format

    def get_destination_data(self):
        # 2. use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]  # destination data from json, prices is key
        return self.destination_data

    def update_destination_data(self):
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
