import requests
import datetime as dt
from pprint import pprint

API_KEY = "dabIEDFSYcJcu5IMt-2VvUs211sQbclM"
TODAY = dt.datetime.now().date()
TRAVEL_DATE = TODAY + dt.timedelta(days=15)
TODAY.strftime("%d/%m/%Y")
TRAVEL_DATE.strftime("%d/%m/%Y")
print(TODAY, TRAVEL_DATE)

HEADERS = {
    'apikey': API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.my_location = "Alaska"

    def get_city_code(self, city):
        flight_params = {
            # 'fly_from': self.my_location,
            'term': city,
            # 'date_from': TODAY,
            # 'date_to': TRAVEL_DATE,
        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=flight_params,
                                headers=HEADERS)
        code = response.json()['locations'][0]['code']
        return code
