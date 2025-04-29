# Day 38 - Python Udemy 100 Days Challenge

## Project: Workout Tracker using Nutritionix and Sheety APIs
This project automates the tracking of workouts. You type in your exercise in natural language (e.g., "I ran 5 km"), and it logs the details like duration, calories burned, etc., into a Google Sheet using Nutritionix and Sheety APIs.

## What It Does
- Parses natural language input to identify exercises and related data.
- Fetches calories burned, duration, and more using the **Nutritionix API**.
- Logs the workout data into a **Google Sheet** via the **Sheety API**.

## Features
- Natural language workout entry ("I did 30 minutes of yoga")
- Calculates exercise metrics automatically
- Sends data to a Google Sheet for persistent logging
- Easily extensible and customizable

## Concepts Practiced
- NLP-based input parsing
- API usage and authorization
- Interfacing with Google Sheets via Sheety
- JSON formatting and response parsing
- HTTP methods and headers

## File Structure
```
day38/
├── main.py        # Core logic for nutrition and workout tracking
├── README.md      # Project documentation
```

## How It Works
1. **Input Workout in Plain English**
   ```python
   user_input = input("Tell me which exercises you did: ")
   ```

2. **Send to Nutritionix API**
   ```python
   headers = {
       "x-app-id": APP_ID,
       "x-app-key": API_KEY,
   }
   response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
   exercises = response.json()["exercises"]
   ```

3. **Log Each Exercise to Google Sheet with Sheety**
   ```python
   for exercise in exercises:
       sheet_inputs = {
           "workout": {
               "date": today_date,
               "time": current_time,
               "exercise": exercise["name"].title(),
               "duration": exercise["duration_min"],
               "calories": exercise["nf_calories"]
           }
       }
       requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `datetime`
- Accounts for [Nutritionix](https://developer.nutritionix.com/) and [Sheety](https://sheety.co/)

### Run the Script
```bash
python main.py
```
Replace your credentials (`APP_ID`, `API_KEY`, Sheety token) in the environment or directly in the script (not recommended).

## Summary
This project showcases how powerful and user-friendly automation can be with real-time APIs and spreadsheet integration. It’s a great start for building your own fitness dashboard, habit tracker, or daily activity log.

---
Let me know if you want to auto-send daily summaries via email or build a dashboard from your Google Sheet data! 🏋️📈