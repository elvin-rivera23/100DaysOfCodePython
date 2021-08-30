# references for time: https://stackoverflow.com/questions/4541629/how-to-create-a-datetime-equal-to-15-minutes-ago/4541668
# references for date: https://www.w3schools.com/python/python_datetime.asp
# reference for string split: https://www.w3schools.com/python/ref_string_split.asp

import requests
from flight_data import FlightData
import os
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "My_API_KEY"  # hidden when uploading to github

class FlightSearch:
    def __init__(self):
        self.city_codes = []

    # pass in city name to get destination code
    def get_destination_code(self, city_names):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        for city in city_names:
            query = {"term": city_names, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)   # api request for tequila query
            results = response.json()["locations"]
            # code = "Testing for now"    # just putting this here for now to get Sheety to work
            code = results[0]["code"]  # first element
            self.city_codes.append(code)
        return self.city_codes

    # The next step is to search for the flight prices from London (LON) to all the destinations in the Google Sheet.
    # In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months (
    # 6x30days) time. We're also looking for round trips that return between 7 and 28 days in length. The currency of
    # the price we get back should be in GBP.
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        # if destination exists,that becomes new data, if it reaches index error exit
        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_departure"].split("T")[0],
            )
            # print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
