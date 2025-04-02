import requests
import pandas
import datetime
from twilio.rest import Client

API_KEY = 'c47cee32692a452f9b5663107eb0878e'
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
ps ="?lat=6.753509&lon=80.166114&appid=c47cee32692a452f9b5663107eb0878e"

weather_params = {
    "lat" : 6.753509,
    "lon" : 80.166114, 
    "appid" : API_KEY,
    "cnt" : 5,
}

#sahara weather(location) for test

# weather_params = {
#     "lat" : 14.698391, 
#     "lon" : 30.632751, 
#     "appid" : API_KEY,
#     "cnt" : 4,
# }


response = requests.get(API_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_list = []
hour_list = ''




for item in weather_data["list"] :
    weather_list.append(item["weather"][0])



def is_going_to_rain():
    x = 0
    global hour_list
    for i in range(0,len(weather_list)):
        if int(weather_list[i]["id"]) < 700 :
            hour_list += '-1-'
            x += 1
        else:
            hour_list += '-0-'

    if x != 0 :
        print("take your jacket todayy")
        return True

    else :
        return False



print(hour_list)

if is_going_to_rain() :
    account_sid = 'AC6b135ecffd98acf47e1f73b737990276'
    auth_token = '15ba6131536c1c6c944b910529182185'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+14028258539',
        body=f'hey you will need a jacket today\nhear is your fore cast {hour_list}',
        to='+94712835711'
    )
    print(message.status)