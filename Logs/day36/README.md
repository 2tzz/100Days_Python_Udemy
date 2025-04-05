# Day 36 - Python Udemy 100 Days Challenge

## Project: Stock Trading News Alert
This project checks for major changes in stock prices and sends news articles about the company if a significant change is detected. It combines real-time financial data with news APIs and automates alerting via SMS.

## What It Does
- Fetches recent stock price data (e.g., TSLA) using the Alpha Vantage API.
- Compares yesterday's and the day before yesterday's closing prices.
- If the change is more than a set threshold (e.g., 5%), it fetches the top 3 news articles about the company using the NewsAPI.
- Sends an SMS with the percentage change and news headlines using Twilio.

## Features
- Real-time stock price tracking
- Threshold-based alerts
- News headline integration for context
- SMS alerts for instant notification

## Concepts Practiced
- REST API usage (Alpha Vantage, NewsAPI, Twilio)
- Environment variable management
- String formatting and f-strings
- Data filtering and error handling
- SMS integration

## File Structure
```
day36/
├── main.py        # Core logic
├── README.md      # Documentation
```

## How It Works
1. **Get Stock Price Data**
   ```python
   stock_params = {
       "function": "TIME_SERIES_DAILY",
       "symbol": STOCK,
       "apikey": STOCK_API_KEY,
   }
   response = requests.get(STOCK_ENDPOINT, params=stock_params)
   data = response.json()["Time Series (Daily)"]
   ```
2. **Compare Two Days' Closing Prices**
   ```python
   yesterday = float(data[yesterday_date]["4. close"])
   day_before = float(data[day_before_date]["4. close"])
   diff_percent = abs((yesterday - day_before) / day_before) * 100
   ```
3. **If Significant Change, Get News & Send SMS**
   ```python
   if diff_percent > 5:
       news_response = requests.get(NEWS_ENDPOINT, params=news_params)
       articles = news_response.json()["articles"][:3]
       for article in articles:
           message = client.messages.create(
               body=f"{STOCK}: {up_down}{round(diff_percent)}%\nHeadline: {article['title']}\nBrief: {article['description']}",
               from_="+YourTwilioNumber",
               to="+YourPhoneNumber"
           )
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `twilio`, `datetime`, `os`
- Alpha Vantage API key, NewsAPI key, Twilio credentials

### Run the Script
```bash
python main.py
```
Set the required API keys and credentials as environment variables before running.

## Summary
This project shows how to combine multiple APIs to build a real-world financial alert system. It enhances your Python skills in data handling, condition checking, and user notification through third-party services.

---
Let me know if you want to log results to a file, use email instead of SMS, or track multiple stocks! :)

