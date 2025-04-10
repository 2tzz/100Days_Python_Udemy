import requests
from datetime import datetime

today = str(datetime.now())

date_list = today.split(" ")

date = date_list[0]
time = date_list[1].split(".")[0]


natural_exercise_endpoint =  "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4b62b0bf9f98c5e6082ff771ece0e18c/myWorkouts/workouts"

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

calorie_dict = calorie_data["exercises"][0]



exercise = calorie_dict["name"]
duration = calorie_dict["duration_min"]
calories = calorie_dict["nf_calories"]


sheet_params = {
    "Date" : date,
    "Time" : time,
    "Exercise" : exercise,
    "Duration" : duration,
    "Calories" : calories
}

header_sheety = {
    "Authorization": "Bearer TTtt47"
}

response_sheety = requests.post(sheety_endpoint , headers=header_sheety ,json=sheet_params)
response_sheety.raise_for_status()



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