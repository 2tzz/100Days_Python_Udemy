
---

# ✨ Day 40 – Flight Club ✨

Welcome to **Flight Club**, the second part of our capstone project from the [100 Days of Code – Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. This project enhances the Flight Deal Finder by adding user management and personalized notifications.

---

## 🧳 Project Overview

The Flight Club application performs the following tasks:

1. Collects user information (name and email) via a command-line interface.
2. Stores user data in a Google Sheet using the Sheety API.
3. Checks for flight deals using the Kiwi Tequila API.
4. Sends personalized email alerts to users when deals are found.

---

## 🛠️ Technologies & Skills

- **APIs**: Sheety, Kiwi Tequila
- **HTTP Requests**: Utilizing the `requests` library
- **Environment Variables**: Managing API keys securely
- **Data Modeling**: Custom classes for structured data
- **Email Automation**: Sending emails using `smtplib`

---

## 🗂️ Project Structure



```plaintext
day40/
├── flight_deals_upgraded/
│   ├── data_manager.py        # Manages user and destination data
│   ├── flight_data.py         # Flight data model
│   ├── flight_search.py       # Logic to fetch flights
│   ├── main.py                # Main runner script
│   ├── notification_manager.py# Sends email notifications
│   └── user_interface.py      # Handles user input
├── README.md                  # Project documentation
```



---

## 🚀 How It Works

1. **User Registration**: The `user_interface.py` script collects user information and validates email addresses.

   ```python
   class UserInterface:
       def get_user_info(self):
           print("Welcome to Flight Club.")
           first_name = input("What is your first name? ")
           last_name = input("What is your last name? ")
           email = input("What is your email? ")
           confirm_email = input("Type your email again: ")
           if email == confirm_email:
               return {
                   "firstName": first_name,
                   "lastName": last_name,
                   "email": email
               }
           else:
               print("Emails do not match. Please try again.")
               return None
   ```



2. **Data Management**: The `DataManager` class handles reading from and writing to the Google Sheet.

   ```python
   class DataManager:
       def add_user(self, user_data):
           response = requests.post(
               url=SHEETY_USERS_ENDPOINT,
               json={"user": user_data}
           )
           response.raise_for_status()
   ```



3. **Flight Search & Notification**: The application checks for flight deals and sends personalized emails to users.

   ```python
   class NotificationManager:
       def send_emails(self, users, message):
           with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
               connection.starttls()
               connection.login(user=EMAIL, password=PASSWORD)
               for user in users:
                   connection.sendmail(
                       from_addr=EMAIL,
                       to_addrs=user["email"],
                       msg=f"Subject:New Low Price Flight!\n\nDear {user['firstName']},\n{message}"
                   )
   ```



---

## 📌 Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day40/flight_deals_upgraded
   ```



2. **Install Dependencies**:

   ```bash
   pip install requests
   ```



3. **Set Up Environment Variables**:

   Create a `.env` file in the `flight_deals_upgraded` directory and add your API keys and email credentials:

   ```plaintext
   TEQUILA_API_KEY=your_tequila_api_key
   SHEETY_ENDPOINT=your_sheety_endpoint
   SHEETY_USERS_ENDPOINT=your_sheety_users_endpoint
   EMAIL=your_email@example.com
   PASSWORD=your_email_password
   ```



4. **Run the Application**:

   ```bash
   python main.py
   ```



---

## 📬 Notes

- **API Keys**: Ensure you have valid API keys for both Sheety and Kiwi Tequila.
- **Email Credentials**: Use an app-specific password if you're using Gmail with two-factor authentication.
- **Google Sheet Structure**: Your Google Sheet should have separate tabs for users and destination data.

---

## 🌟 Acknowledgments

This project is inspired by Day 40 of the [100 Days of Code – Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

---

