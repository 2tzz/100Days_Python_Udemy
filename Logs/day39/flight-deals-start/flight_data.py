
from datetime import datetime , timedelta
from flight_search import FlightSearch
import requests

fft = FlightSearch()

data = {'prices': 
        [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, 
         {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, 
         {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, 
         {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, 
         {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, 
         {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, 
         {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, 
         {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, 
         {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]
         }

after_sixmonths_timedate = str(datetime.now() + timedelta(180))

daylst = after_sixmonths_timedate.split(" ")
after_sixmonths_date  = daylst[0]

print(after_sixmonths_date)

class FlightData:
    def __init__(self , string):
        self.my_iata = string
        


    def get_flight_offer(self , datas) :

        itemslist = datas["prices"]
        flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"


        for item in itemslist  :

            all_offers = []
    
            offer_params = {
                "originLocationCode" : f"{self.my_iata}", 
                "destinationLocationCode" : item["iataCode"], 
                "departureDate" : f"{datetime.today().date() + timedelta(1)}", 
                "returnDate" : f"{after_sixmonths_date}", 
                "adults" : 1,
                "nonStop" : "true", 
                "currencyCode" : "GBP" ,
                "maxPrice" : int(item["lowestPrice"])
            }

            token = fft._get_new_token()

            header = {
            "Authorization": f"Bearer {token}"
            }

            response_offers = requests.get(url=flight_offer_endpoint , headers=header , params=offer_params)
            response_offers.raise_for_status()
            data_offer = response_offers.json()
            all_offers.append(data_offer)
        return all_offers
