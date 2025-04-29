

# ✨ Day 39 – Flight Deal Finder ✨

Welcome to the **Flight Deal Finder** project, crafted as part of the [100 Days of Code – Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. This capstone project automates the process of tracking flight deals and notifies users when prices drop below a specified threshold. ([mannekeenpis/100-days-of-python - GitHub](https://github.com/mannekeenpis/100-days-of-python?utm_source=chatgpt.com))

---

##  Project Overview

This application performs the following tasks:

1. Retrieves city names and IATA codes from a Google Sheet via the Sheety API.
2. Uses the Kiwi Tequila API to check for the lowest flight prices.
3. Compares results with stored price thresholds.
4. Sends email alerts when cheaper deals are found. ([Anyone get stuck on Day 39 of 100 days of code python? - Reddit](https://www.reddit.com/r/learnpython/comments/1cn7shd/anyone_get_stuck_on_day_39_of_100_days_of_code/?utm_source=chatgpt.com))

---

## 🛠 Technologies & Skills

- **APIs**: Sheety, Kiwi Tequila
- **HTTP Requests**: Utilizing the `requests` library
- **Environment Variables**: Managing API keys securely
- **Data Modeling**: Custom classes for structured data
- **Email Automation**: Sending emails using `smtplib` ([100 Days of Code: A Challenging Complete Python Pro Bootcamp](https://www.udemy.com/course/excellent-python-3-bootcamp-in-2023/?srsltid=AfmBOoqEdKeUFxmdic_Zysn1c1CBY3qOIrKzxXLMe1c-0g_feekzRtVl&utm_source=chatgpt.com))

---

## 🗂 Project Structure


```plaintext
day39/
├── flight_data.py          # Flight data model
├── flight_search.py        # Logic to fetch flights
├── data_manager.py         # Interacts with Google Sheets
├── notification_manager.py # Sends email notifications
├── main.py                 # Main runner script
├── README.md               # Project documentation
```


---

##  How It Works

1. **Data Retrieval**: The `DataManager` class fetches city names and IATA codes from a Google Sheet via the Sheety API.

   ```python
   class DataManager:
       def get_destination_data(self):
           response = requests.get(SHEETY_ENDPOINT)
           data = response.json()
           self.destination_data = data["prices"]
           return self.destination_data
   ```


2. **Flight Search**: The `FlightSearch` class uses the Kiwi Tequila API to find the lowest flight prices for each city. ([Anyone get stuck on Day 39 of 100 days of code python? - Reddit](https://www.reddit.com/r/learnpython/comments/1cn7shd/anyone_get_stuck_on_day_39_of_100_days_of_code/?utm_source=chatgpt.com))

   ```python
   class FlightSearch:
       def get_flight_price(self, origin_city_code, destination_city_code, from_time, to_time):
           headers = {"apikey": TEQUILA_API_KEY}
           query = {
               "fly_from": origin_city_code,
               "fly_to": destination_city_code,
               "date_from": from_time.strftime("%d/%m/%Y"),
               "date_to": to_time.strftime("%d/%m/%Y"),
               "nights_in_dst_from": 7,
               "nights_in_dst_to": 28,
               "flight_type": "round",
               "one_for_city": 1,
               "max_stopovers": 0,
               "curr": "USD"
           }
           response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=query)
           data = response.json()["data"][0]
           return data["price"]
   ```


3. **Price Comparison & Notification**: If a found flight price is lower than the stored threshold, the `NotificationManager` class sends an email alert.

   ```python
   class NotificationManager:
       def send_email(self, message):
           with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
               connection.starttls()
               connection.login(user=EMAIL, password=PASSWORD)
               connection.sendmail(
                   from_addr=EMAIL,
                   to_addrs=EMAIL,
                   msg=f"Subject:New Low Price Flight!\n\n{message}"
               )
   ```


---

## 📌 Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day39
   ```


2. **Install Dependencies**:

   ```bash
   pip install requests
   ```


3. **Set Up Environment Variables**:

   Create a `.env` file in the `day39` directory and add your API keys and email credentials:

   ```plaintext
   TEQUILA_API_KEY=your_tequila_api_key
   SHEETY_ENDPOINT=your_sheety_endpoint
   EMAIL=your_email@example.com
   PASSWORD=your_email_password
   ```


4. **Run the Application**:

   ```bash
   python main.py
   ```


---

##  Notes

- **API Keys**: Ensure you have valid API keys for both Sheety and Kiwi Tequila.
- **Email Credentials**: Use an app-specific password if you're using Gmail with two-factor authentication.
- **Google Sheet Structure**: Your Google Sheet should have columns for city names, IATA codes, and price thresholds. ([Anyone get stuck on Day 39 of 100 days of code python? - Reddit](https://www.reddit.com/r/learnpython/comments/1cn7shd/anyone_get_stuck_on_day_39_of_100_days_of_code/?utm_source=chatgpt.com))

---

##  Acknowledgments

This project is inspired by Day 39 of the [100 Days of Code – Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. ([mannekeenpis/100-days-of-python - GitHub](https://github.com/mannekeenpis/100-days-of-python?utm_source=chatgpt.com))

---

