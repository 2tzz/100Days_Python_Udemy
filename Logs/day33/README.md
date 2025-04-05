# Day 33 - Python Udemy 100 Days Challenge

## Project: ISS Overhead Notifier ✨
This project was built as part of the **100 Days of Code - Python Udemy Challenge**, focused on using API integration, automation, and condition-based logic. The goal is to notify the user via email when the **International Space Station (ISS)** is overhead during nighttime.

## What It Does
- Fetches **real-time ISS location data** using the Open Notify API.
- Checks **local sunrise and sunset times** via the Sunrise-Sunset API.
- Sends an **email alert** when the ISS is overhead and it's dark outside (great for spotting the ISS!).

## Features
- Real-time geolocation comparison with ISS position
- Daylight checking to ensure it's nighttime
- Automated **email notifications** when conditions are met
- Runs on a **loop with time delays** to check every 60 seconds

## Concepts Practiced
- API requests with `requests`
- Handling JSON data
- Datetime manipulation
- Email automation with `smtplib`
- Looping and conditional logic

## File Structure
```
day33/
├── main.py          # Main Python script
├── README.md        # Project documentation
```

## How It Works
1. **Check ISS Position**
   ```python
   response = requests.get(url="http://api.open-notify.org/iss-now.json")
   position = response.json()["iss_position"]
   iss_lat = float(position["latitude"])
   iss_long = float(position["longitude"])
   ```
2. **Check If ISS Is Nearby & It's Night**
   ```python
   def is_iss_overhead():
       return (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LONG - 5 <= iss_long <= MY_LONG + 5)

   def is_night():
       return now_hour >= sunset or now_hour <= sunrise
   ```
3. **Send Email Notification**
   ```python
   if is_iss_overhead() and is_night():
       with smtplib.SMTP("smtp.gmail.com", 587) as connection:
           connection.starttls()
           connection.login(MY_EMAIL, MY_PASSWORD)
           connection.sendmail(
               from_addr=MY_EMAIL,
               to_addrs=MY_EMAIL,
               msg="Subject: Look Up!\n\nThe ISS is above you in the sky!"
           )
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `smtplib`, `datetime`, `time`

### Run the Script
```bash
python main.py
```
Make sure to:
- Replace `MY_EMAIL`, `MY_PASSWORD`, `MY_LAT`, and `MY_LONG` with your own details.
- Enable **less secure app access** or generate an **App Password** if using Gmail.

## Hosting
You can host this script on **PythonAnywhere** to run 24/7 by adding it as a scheduled task.

## Email Preview
```
Subject: Look Up!

The ISS is above you in the sky!
```

## Summary
This project is a great example of combining multiple APIs, time-based logic, and email automation to create a real-world useful script. It was a fun exercise in thinking about conditions, user experience, and real-time data.

---
Let me know if you want to enhance the logic or add GUI/notification support! :)

