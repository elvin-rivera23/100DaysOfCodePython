import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "My_API_KEY"  # hidden when uploading to github

class FlightSearch:

    # pass in city name to get destination code
    def get_destination_code(self, city_name):
        code = "Testing for now"    # just putting this here for now to get Sheety to work
        return code