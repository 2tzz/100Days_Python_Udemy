import requests
from pprint import pprint



api_endpoint_flight = "https://test.api.amadeus.com/v1/security/oauth2/token"

api_endpoint_city = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

headers_params = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

body_params = {
    "grant_type" : "client_credentials" ,
    "client_id" : "lGdiH06kL6dsYtRZBFKG5HyG3draefb8" , 
    "client_secret" : "sVWw6lAs6Xj5uxGj"
    }

response = requests.post(url=api_endpoint_flight , headers=headers_params ,data=body_params )
data = response.json()
new_token = data["access_token"]

print(new_token)


headerx = {
    "Authorization": f"Bearer {new_token}"
}

city_params =  {
    "keyword" : "PARIS",
    "max" : 1
      }


response_city = requests.get(url=api_endpoint_city , headers=headerx , params=city_params)

data_city = response_city.json()


pprint(data_city)