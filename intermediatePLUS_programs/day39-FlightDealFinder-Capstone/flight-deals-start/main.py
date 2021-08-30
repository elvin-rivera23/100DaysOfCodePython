# Elvin Rivera
# 8/29/21
#
# Description: Appliction for finding flight deals. Capstone project: OOP, APIs, datetime, List and Dictionary Comprehensions

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# Resources: https://sheety.co , https://partners.kiwi.com , https://tequila.kiwi.com/portal/login ,
# https://www.twilio.com/docs/sms


# Pass everything stored in the "prices" key back to the main.py file
# and store it in a variable called sheet_data, so that you can print the sheet_data from main.py

from data_manager import DataManager

data_manager = DataManager()  # initialize object data_manager
sheet_data = data_manager.get_destination_data()  # call method to get destination data
# print(sheet_data)


# In main.py check if sheet_data contains any values for the "iataCode" key. If not, then the IATA Codes column is
# empty in the Google Sheet. In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code. You should use the response
# from the FlightSearch class to update the sheet_data dictionary.

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()  # initialize flight search object
    # sheet data is in dictionary/json format
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    # format sheet
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()