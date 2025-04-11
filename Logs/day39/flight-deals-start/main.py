#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

dt  = DataManager()
fs = FlightSearch()

# flight_data = dt.get_data()

dt.put_iata("thiyura")

# fs._get_iata("COLOMBO")



