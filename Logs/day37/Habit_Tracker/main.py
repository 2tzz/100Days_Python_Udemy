import requests
from datetime import datetime

today = datetime(year=2025 , month=4 , day=6)

USER_NAME = "thiyura"
TOKEN = "tT47tt74TT77tt44"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph001"
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph001/20250406"
pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph001/20250406"
date = "20250407"






user_params = {
    "token" : TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService" : "yes" ,
    "notMinor" : "yes",
}
graph_config = {
    "id" : "graph001",
    "name" : "cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "15"

}

pixel_config_update  = {
    "quantity" : "4"
}

headders = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_config_update , headers=headders)
response = requests.delete(url=pixel_delete_endpoint , headers=headders)
print(response.text)