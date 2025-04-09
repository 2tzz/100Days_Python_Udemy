import requests
import datetime


natural_exercise_endpoint =  "https://trackapi.nutritionix.com/v2/natural/exercise"

API_KEY = '138e510a7cf838f4b6c90dd45b70538f'
APP_ID = 'd13ef7a4'

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

user_input =  input("Enter the exercises you've done today : ")

exercise_params = {
    "query": user_input
}



response = requests.post(natural_exercise_endpoint , headers=header ,json=exercise_params)
response.raise_for_status()
calorie_data = response.json()

print(calorie_data)


# url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# headers = {
#     'Content-Type': 'application/json',
#     'x-app-id': 'd13ef7a4',
#     'x-app-key': '138e510a7cf838f4b6c90dd45b70538f'
# }
# data = {
#     'query': 'swam for 1 hour'
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.status_code)
# print(response.json())