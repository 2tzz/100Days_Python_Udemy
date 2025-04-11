import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("SHEETY_API_KEY")

class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/4b62b0bf9f98c5e6082ff771ece0e18c/flightDeals/prices"
        self.header_sheety = {
            "Authorization": api_key
        }
    

    def get_data(self) :
        response_sheety = requests.get(self.sheety_endpoint  , headers=self.header_sheety)
        response_sheety.raise_for_status()
        flight_data = response_sheety.json()
        return flight_data

    def put_iata(self , string):
        data = self.get_data()
        items = data["prices"]

       
        for row in items :
            row_id = row["id"]
            city = row["city"]
            update_url = f"{self.sheety_endpoint}/{row_id}"
            body = {
                "price": {
                    "iataCode": string
                    }
                }
            
            update_response = requests.put(update_url, json=body, headers=self.header_sheety)
            update_response.raise_for_status()

   



