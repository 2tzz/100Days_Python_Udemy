# Day 39 - Flight Deal Finder

This project was created as part of the **100 Days of Code - Python (Udemy)** challenge. It helps automate tracking of **cheap flight deals** using real-world APIs and notifies the user when prices drop below a set threshold.

## What It Does

- Retrieves city names and IATA codes from a Google Sheet via Sheety API.
- Uses the Kiwi Tequila API to check for the lowest flight prices.
- Compares results with stored price thresholds.
- Sends email alerts when cheaper deals are found.

## Skills Practiced

- Working with multiple APIs (Tequila Kiwi, Sheety)
- HTTP requests and headers
- Environment variables for API security
- Data modeling with custom classes
- Email automation using `smtplib`

## File Structure

day39/ ├── flight_data.py # Flight data model ├── flight_search.py # Logic to fetch flights ├── data_manager.py # Interacts with Google Sheets ├── notification_manager.py # Sends email notifications ├── main.py # Main runner script ├── README.md

python
Copy
Edit

## How It Works

1. Loads city list and target prices from a Google Sheet.
2. If IATA codes are missing, the program fetches and updates them.
3. Searches for flights from the home city to each destination.
4. If a flight is found under the threshold, an email is sent.

### Example Code Snippet

```python
if flight_data.price < row["lowestPrice"]:
    notification_manager.send_email(
        message=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city} to {flight_data.destination_city}, from {flight_data.out_date} to {flight_data.return_date}."
    )
Email Notification Example
vbnet
Copy
Edit
Subject: Low price alert!

Only £109 to fly from London to Rome, from 2024-06-10 to 2024-06-20.
Requirements
Python 3.x

Environment variables:

TEQUILA_API_KEY

SHEETY_ENDPOINT and token

Email credentials (MY_EMAIL, MY_PASSWORD)

Install required packages:

bash
Copy
Edit
pip install requests
Optional Improvements
Add SMS alerts via Twilio

Schedule the script with PythonAnywhere or cron

Track more cities or flexible date ranges
