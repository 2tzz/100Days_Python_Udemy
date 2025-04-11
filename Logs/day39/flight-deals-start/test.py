import requests





api_endpoint_flight = "https://test.api.amadeus.com/v1/security/oauth2/token"

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
print(data)
new_token = data["access_token"]

print(new_token)
