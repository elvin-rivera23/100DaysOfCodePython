import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "My_API_KEY"  # hidden when uploading to github

class FlightSearch:

    # pass in city name to get destination code
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)   # api request for tequila query
        results = response.json()["locations"]
        # code = "Testing for now"    # just putting this here for now to get Sheety to work
        code = results[0]["code"]  # first element
        return code