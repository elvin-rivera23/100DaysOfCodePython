# Elvin Rivera
# 8/29/21
#
# Description: Appliction for finding flight deals. Capstone project: OOP, APIs, datetime, List and Dictionary Comprehensions

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# Resources: https://sheety.co , https://partners.kiwi.com , https://tequila.kiwi.com/portal/login ,
# https://www.twilio.com/docs/sms
# Airport code: https://en.wikipedia.org/wiki/IATA_airport_code


# Pass everything stored in the "prices" key back to the main.py file
# and store it in a variable called sheet_data, so that you can print the sheet_data from main.py

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()  # initialize object data_manager
sheet_data = data_manager.get_destination_data()  # call method to get destination data
# print(sheet_data)
flight_search = FlightSearch()  # initialize flight search object
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# In main.py check if sheet_data contains any values for the "iataCode" key. If not, then the IATA Codes column is
# empty in the Google Sheet. In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code. You should use the response
# from the FlightSearch class to update the sheet_data dictionary.

# if sheet_data[0]["iataCode"] == "":
#     # sheet data is in dictionary/json format
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     # print(f"sheet_data:\n {sheet_data}")
#     # print(sheet_data)
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]   # list comprehension
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# dictionary comprehension
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"],
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    print(flight.price)

    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only ??{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. "
        if flight.stop_overs > 0:
            message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)
        # notification_manager.send_sms(message)