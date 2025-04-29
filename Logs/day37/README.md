# Day 37 - Python Udemy 100 Days Challenge

## Project: Habit Tracker Using Pixela API
This project builds a **habit tracking automation** tool that integrates with the Pixela API. It allows users to create accounts, set up graphs, and post daily activity data like coding, exercise, or any measurable habit.

## What It Does
- Creates a user and a graph on Pixela (once per user).
- Posts daily progress data to the graph (like hours coded or steps walked).
- Updates or deletes data if needed.

## Features
- Pixela API integration for visual habit tracking
- Create, update, and delete tracking pixels (daily logs)
- Customizable graph color, type, and title
- Automates interaction via Python

## Concepts Practiced
- Working with REST APIs
- Authorization headers and JSON payloads
- String formatting
- Handling HTTP methods: POST, PUT, DELETE

## File Structure
```
day37/
├── main.py        # Handles user creation, graph setup, and pixel management
├── README.md      # Project documentation
```

## How It Works
1. **Create a User (once)**
   ```python
   user_params = {
       "token": TOKEN,
       "username": USERNAME,
       "agreeTermsOfService": "yes",
       "notMinor": "yes",
   }
   requests.post(url=PIXELA_ENDPOINT, json=user_params)
   ```

2. **Create a Graph**
   ```python
   graph_params = {
       "id": GRAPH_ID,
       "name": "Coding Tracker",
       "unit": "hour",
       "type": "float",
       "color": "shibafu",
   }
   requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
   ```

3. **Add or Update a Pixel (Daily Log)**
   ```python
   pixel_data = {
       "date": today_date,
       "quantity": "3.5",
   }
   requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_data, headers=headers)
   ```

4. **Update or Delete (Optional)**
   ```python
   requests.put(url=PIXEL_UPDATE_ENDPOINT, json=new_data, headers=headers)
   requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `datetime`

### Run the Script
```bash
python main.py
```
Make sure to:
- Replace `USERNAME`, `TOKEN`, and `GRAPH_ID` with your Pixela credentials.
- Adjust the habit and quantity according to your tracking goals.

## Summary
This project is a great example of how APIs can be used to automate personal development tracking. It’s an ideal stepping stone to creating habit dashboards, integrating with calendars, or even building reminders.

---
Let me know if you’d like to integrate it with Google Sheets, Telegram reminders, or schedule it with cron or PythonAnywhere! :)

