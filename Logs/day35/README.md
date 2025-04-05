# Day 35 - Python Udemy 100 Days Challenge

## Project: Rain Alert with SMS Notification
This project is a weather notification tool that checks your location for rain and sends you an SMS if it's going to rain today. It uses the OpenWeatherMap API and Twilio for SMS alerts.

## What It Does
- Connects to OpenWeatherMap API to fetch 12-hour forecast data.
- Checks each hour for potential rain conditions.
- Sends an SMS notification if rain is detected in the upcoming hours.

## Features
- Weather forecast parsing with rain detection
- SMS notification via Twilio
- Can be scheduled to run daily or hourly

## Concepts Practiced
- Environment variables and API keys
- RESTful API usage
- Working with JSON and weather codes
- SMS automation using `twilio`
- Data filtering and conditional logic

## File Structure
```
day35/
├── main.py        # Main logic for weather check and SMS sending
├── README.md      # Documentation file
```

## How It Works
1. **Get Weather Data**
   ```python
   response = requests.get(OWM_Endpoint, params=weather_params)
   weather_data = response.json()
   ``
2. **Check for Rain**
   ```python
   for hour_data in weather_data["hourly"][:12]:
       condition_code = hour_data["weather"][0]["id"]
       if int(condition_code) < 700:
           will_rain = True
   ```
3. **Send SMS**
   ```python
   if will_rain:
       client = Client(account_sid, auth_token)
       message = client.messages.create(
           body="It’s going to rain today. Don’t forget your umbrella! ☔",
           from_="+YourTwilioNumber",
           to="+YourPhoneNumber"
       )
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `twilio`, `os`
- Twilio account and OpenWeatherMap API key

### Run the Script
```bash
python main.py
```
Set your `account_sid`, `auth_token`, `TWILIO_PHONE`, `MY_PHONE`, and `OWM_API_KEY` as environment variables.

## Summary
This script helps build your automation skills and shows how real-time data and third-party services like Twilio can enhance daily life with useful alerts. It’s a great practical application of Python for personal utility.

---
Let me know if you’d like to add email notifications or integrate with Telegram or Discord instead! :)
