#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData , data

dt  = DataManager()
fs = FlightSearch()
fd = FlightData("LON")

flight_sheet_data = dt.get_data()
# print(flight_data)

# dt.put_iata()

# fs._get_iata("COLOMBO")

flight_offers = fd.get_flight_offer(flight_sheet_data)

print(flight_offers)

