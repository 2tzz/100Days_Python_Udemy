# Day 32 - Python Udemy 100 Days Challenge

## Overview
This project is part of the **100 Days of Python Udemy Course**, specifically focusing on **Day 32**. The challenge was to create an **Email Notification System for Rain Alerts**, and I successfully completed it using my own logical approach with only **one hint**, making this project a result of my independent problem-solving skills.

## Key Features
- **Weather API Integration** to fetch real-time weather data.
- **Automated Email Alerts** for notifying about rainy conditions.
- **SMTP Authentication** to securely send emails.
- **Efficient Logic** for checking and filtering relevant weather conditions.

## My Unique Approach
Unlike following direct solutions, I designed and structured the code based on my own thought process. The logic flow, API calls, and email automation were all implemented with minimal guidance, showcasing my ability to independently develop and debug Python applications.

## Code Snippets & Highlights

### **1. Fetching Weather Data from API**
This function retrieves weather details from an API and checks for rain conditions.
```python
import requests

API_KEY = "your_api_key_here"
LAT, LON = 51.5074, -0.1278  # Example: London Coordinates

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
)
data = response.json()

# Check for rain in upcoming hours
for hour_data in data["list"][:12]:  # Next 12 hours
    if "rain" in hour_data["weather"][0]["main"].lower():
        will_rain = True
        break
```
✅ *Efficiently processes API data to detect upcoming rainy weather.*

### **2. Sending an Email Alert**
This function sends an automated email if rain is detected.
```python
import smtplib

EMAIL = "your_email@example.com"
PASSWORD = "your_password"

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure connection
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="recipient@example.com",
            msg="Subject:Rain Alert!\n\nBring an umbrella. It will rain today!"
        )
```
✅ *Uses SMTP securely to send weather alerts with proper authentication.*

## Installation & Setup

### **Prerequisites**
Ensure you have the following installed before running the project:
- **Python 3.x**
- **Requests** for API calls:
  ```sh
  pip install requests
  ```

### **Steps to Run the Project**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day32
   ```

2. **Set Up API Key**
   - Sign up at [OpenWeather](https://openweathermap.org/) and get an API key.
   - Replace `your_api_key_here` in the script.

3. **Run the Python Script**
   ```sh
   python main.py
   ```

## File Structure
```
Logs/day32/
│── main.py          # Main Python script for rain alert system
│── README.md        # Documentation for the project
```

## Usage
- Run the script to check for rain alerts.
- If rain is expected, an email notification will be sent automatically.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your fork and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please open an issue on the GitHub repository.

---

Let me know if you need any modifications! 🚀

