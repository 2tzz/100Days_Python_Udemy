
---

# Day 46 – Scraping the Billboard Hot 100

This project is part of Day 46 from the *100 Days of Code: Python Bootcamp*.  
The goal is to **scrape Billboard's Hot 100 chart** and collect the top songs at a specific historical date.

---

## Project Overview

- Use **BeautifulSoup** and **requests** to scrape the Billboard Hot 100 page.
- Input a **date** (YYYY-MM-DD format).
- Scrape and list the **top 100 songs** from that day.
- Prepare the list for future use (e.g., creating a Spotify playlist).

---

## Setup Instructions

First, install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## How It Works

### 1. User Input for Date

The script asks the user for a date:

```python
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
```

Example:  
```
2000-08-12
```

---

### 2. Fetching Billboard Page

The script builds the correct URL and sends a request:

```python
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
website_html = response.text
```

---

### 3. Parsing Songs

Using BeautifulSoup, it extracts all song titles:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(website_html, "html.parser")
song_tags = soup.select("li ul li h3")
```

Filtering and cleaning the text:

```python
songs = [song.getText().strip() for song in song_tags]
```

Result: A list of the **Top 100 Songs** at that time.

---

## Example Output

```text
['Incomplete', 'It’s Gonna Be Me', 'Bent', 'Try Again', 'Big Pimpin’', ..., 'I Hope You Dance']
```

A clean Python list with 100 song titles ready for further processing.

---

## Folder Structure

```
day46/
├── Scraping the Billboard Hot 100/
│   └── main.py
```

- **main.py**: Full code to scrape the Billboard Hot 100 songs.

---

## Useful References

- [Billboard Hot 100 Chart](https://www.billboard.com/charts/hot-100/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Docs](https://requests.readthedocs.io/en/latest/)

---

## Summary

In this project, you practiced:

- Constructing dynamic URLs based on user input
- Scraping real-world structured data from a popular music website
- Cleaning and formatting extracted data for future automation

This project also prepares you for **Spotify API integration** in upcoming lessons!

---
