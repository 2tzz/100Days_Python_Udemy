import requests


USER_NAME = "thiyura"
TOKEN = "tT47tt74TT77tt44"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph001"
date = 20250407

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
    "date" : date,
    "quantity" : 1

}

headders = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=pixel_config, json=graph_config , headers=headders)

print(response.text)