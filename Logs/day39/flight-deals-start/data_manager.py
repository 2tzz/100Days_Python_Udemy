import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/4b62b0bf9f98c5e6082ff771ece0e18c/flightDeals/prices"
        self.header_sheety = {
            "Authorization": "Bearer flightTt47"
        }
    

    def get_data(self) :
        response_sheety = requests.get(self.sheety_endpoint  , headers=self.header_sheety)
        response_sheety.raise_for_status()
        flight_data = response_sheety.json()
        return flight_data






