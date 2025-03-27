

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()


# latitude = response.json()['iss_position']['latitude']
# longitude = response.json()['iss_position']['longitude']

# iss_position = (latitude , longitude)

# # print(iss_position)

# parameters = {
#     "lat" : MY_LAT,
#     "lng" : MY_LONG,
#     "formatted" : 0
# }


# response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]

# sunrise_hour = sunrise.split("T")[1].split(":")[0]
# sunset_hour = sunset.split("T")[1].split(":")[0]
# print(f"sunrise : {sunrise_hour} \nsunset : {sunset_hour}")

# time_now = datetime.now(timezone.utc)

# print(time_now)