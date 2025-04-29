
---

# Day 47 – Amazon Price Tracker

This project is part of Day 47 from the *100 Days of Code: Python Bootcamp*.  
The goal is to **track the price** of a product on Amazon and send an **email alert** when it drops below a set target.

---

## How It Works

- Scrapes product details (title and price) using `requests` and `BeautifulSoup`.
- Compares the current price with your desired price.
- Sends an email notification if the price drops.

---

## Setup Instructions

1. Install required libraries:

```bash
pip install requests beautifulsoup4 lxml smtplib
```

2. Set up your environment with:
   - Your target Amazon product URL
   - Email address and app password (for sending emails)

---

## Example Code Snippet

```python
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/PRODUCT_ID"
headers = {
    "User-Agent": "Your User Agent",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class_="a-price-whole").get_text()
```

---

## Folder Structure

```
day47/
├── Amazon_price_tracker/
│   └── main.py
```

---

## Notes

- This project may require frequent updates to headers (Amazon blocks bots).
- Always check Amazon's Terms of Service before scraping.

---
