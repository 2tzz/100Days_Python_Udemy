# Day 32 - Python Udemy 100 Days Challenge

## Overview
This project is part of the **100 Days of Python Udemy Course**, specifically focusing on **Day 32**. The challenge was to create a **Birthday Wish Sender**, and I successfully completed it using my own logical approach with only **one hint**, making this project a result of my independent problem-solving skills.

## Key Features
- **Automated Birthday Email System** to send personalized birthday wishes.
- **CSV-based Contact Management** for storing birthday details.
- **SMTP Authentication** for secure email sending.
- **Randomized Messages** to make each wish unique.
- **Deployment on PythonAnywhere** for automated execution without manual intervention.

## My Unique Approach
Unlike following direct solutions, I designed and structured the code based on my own thought process. The logic flow, data handling, and email automation were all implemented with minimal guidance, showcasing my ability to independently develop and debug Python applications.

## Code Snippets & Highlights

### **1. Reading Birthday Data from CSV**
This function reads the birthday details from a CSV file and checks if today matches any birthday.
```python
import pandas as pd
import datetime

# Load birthday data
birthdays = pd.read_csv("birthdays.csv")
today = datetime.datetime.now()

# Find today's birthdays
for _, row in birthdays.iterrows():
    if row['month'] == today.month and row['day'] == today.day:
        send_birthday_email(row['name'], row['email'])
```
✅ *Efficiently processes CSV data to find birthdays that match the current date.*

### **2. Sending a Personalized Birthday Email**
This function sends an automated birthday greeting via email.
```python
import smtplib
import random

EMAIL = "your_email@example.com"
PASSWORD = "your_password"

def send_birthday_email(name, recipient_email):
    with open("messages.txt") as file:
        messages = file.readlines()
    message = random.choice(messages).replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday!\n\n{message}"
        )
```
✅ *Ensures personalized and secure email delivery with randomly selected messages.*

## Hosting on PythonAnywhere
To ensure the script runs automatically every day, I deployed it on **PythonAnywhere** by setting up a scheduled task. Follow these steps to host it:

1. **Create an Account on PythonAnywhere**
   - Sign up at [PythonAnywhere](https://www.pythonanywhere.com/).

2. **Upload Your Project Files**
   - Navigate to the "Files" section and upload `main.py`, `birthdays.csv`, and `messages.txt`.

3. **Schedule a Daily Task**
   - Go to the "Tasks" section and add a new scheduled task.
   - Set it to run `python3 /home/yourusername/main.py` at your desired time.

This ensures the script runs automatically every day without needing to manually execute it.

## Installation & Setup

### **Prerequisites**
Ensure you have the following installed before running the project:
- **Python 3.x**
- **Pandas** for data handling:
  ```sh
  pip install pandas
  ```

### **Steps to Run the Project Locally**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day32
   ```

2. **Set Up Email Credentials**
   - Update `EMAIL` and `PASSWORD` in the script with your credentials.
   - Allow **Less Secure Apps** on your email provider if needed.

3. **Run the Python Script**
   ```sh
   python main.py
   ```

## File Structure
```
Logs/day32/
│── main.py          # Main Python script for birthday wish sender
│── birthdays.csv    # Contact list with names and birthdays
│── messages.txt     # Pre-written birthday message templates
│── README.md        # Documentation for the project
```

## Usage
- Run the script to automatically check for birthdays.
- If a birthday matches today's date, an email is sent with a personalized wish.
- Deploy on PythonAnywhere to run automatically daily.

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
