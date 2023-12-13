# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from pprint import pprint
import requests
from data_manager import DataManager

data_mngr = DataManager()
sheet_data = data_mngr.get_data()
pprint(sheet_data)
flight_srch = FlightSearch()
if sheet_data[0]['iataCode'] == '':
    for city in sheet_data:
        city_code = flight_srch.get_city_code(city=city['city'])
        city['iataCode'] = city_code

data_mngr.destination_data = sheet_data
data_mngr.update_destination_codes()
print(sheet_data)
