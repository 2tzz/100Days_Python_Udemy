#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint

dt  = DataManager()

flight_data = dt.get_data()
pprint(flight_data["prices"])