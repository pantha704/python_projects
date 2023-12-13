from pprint import pprint
import json
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/de02017935ae516e43c746f6aebbd6a0/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': ''
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
            # response = requests.put(url=f"{self.url}/{id}", json=sheet)
        # response2 = requests.get(url=self.url)
        # pprint(sheet)
