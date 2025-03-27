import requests
from datetime import datetime , timezone

MY_LAT = 6.753509
MY_LONG = 80.166114

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# iss_latitude = float(data["iss_position"]["latitude"])
# iss_longitude = float(data["iss_position"]["longitude"])

iss_latitude = 10.653265
iss_longitude = 78.562314


if iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5 :
    if iss_longitude > MY_LONG -5 and iss_longitude < MY_LONG + 5 :

        print("hellow")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(f"sunrise : {sunrise} \nsunset : {sunset}")

time_now = datetime.now(timezone.utc)

print(time_now.hour)