import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
api_key = os.getenv("FLIGHT_API_KEY")
api_seacret = os.getenv("FLIGHT_SECRET")

class FlightSearch:


    def __init__(self):
        self._api_key = api_key
        self._api_secret = api_seacret
        self._token = self._get_new_token()
    
    def _get_new_token(self) :

        api_endpoint_flight = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers_params = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body_params = {
            "grant_type" : "client_credentials" ,
            "client_id" : api_key , 
            "client_secret" : api_seacret
        }

        response = requests.post(url=api_endpoint_flight , headers=headers_params ,data=body_params )
        data = response.json()
        pprint(data)
        new_token = data["access_token"]
        return new_token