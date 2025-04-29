
---

# Day 45 – Web Scraping with BeautifulSoup

Welcome to Day 45 of the *100 Days of Code: Python Bootcamp*!  
Today we dive into **web scraping**, a method to extract data from websites automatically using **BeautifulSoup** and **requests**.

---

## Topics Covered

- Sending HTTP requests using `requests`
- Parsing and traversing HTML content with `BeautifulSoup`
- Selecting and extracting specific elements
- A mini project: Scraping a "Top 100 Movies" list

---

## Setup Instructions

First, install the required libraries:

```bash
pip install beautifulsoup4 requests
```

---

## Example Code

### Fetching HTML content

```python
import requests

response = requests.get("https://news.ycombinator.com/")
webpage_html = response.text
```

This sends a `GET` request and stores the HTML content.

---

### Parsing HTML with BeautifulSoup

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage_html, "html.parser")
```

Creates a `soup` object that allows us to navigate and search the HTML easily.

---

### Extracting Data

```python
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())         # Print the visible text
    print(tag.get("href"))        # Print the link URL
```

- `find_all(name="a")`: Finds all anchor (`<a>`) tags.
- `getText()`: Extracts the text inside a tag.
- `get("href")`: Extracts the link.

---

## Mini Project – Scrape Top 100 Movies

In the `100movies/main.py`:

1. **Target Website**: [Empire Online's Top 100 Movies](https://www.empireonline.com/movies/features/best-movies-2/).
2. **Goal**: Extract the movie titles and save them into a `.txt` file.

Example snippet:

```python
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles[::-1]:  # Reversing to start from #1
        file.write(f"{movie}\n")
```

- `find_all(name="h3", class_="title")`: Looks for all movie title headers.
- We **reverse** the list so the top movie (#1) comes first.

---

## Folder Structure

```
day45/
├── 100movies/
│   └── main.py
├── bs4-start(web scraping)/
│   └── main.py
```

- **bs4-start(web scraping)/main.py**: Basic BeautifulSoup practice.
- **100movies/main.py**: Complete movie scraping project.

---

## Useful Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
- [Python Web Scraping Guide (W3Schools)](https://www.w3schools.com/python/python_web_scraping.asp)

---

## Summary

By the end of Day 45, you will know how to:

- Send web requests and get page content
- Parse and navigate HTML trees
- Find and extract specific data
- Save extracted information for later use

This skill is powerful for building bots, data collection tools, and automation scripts.

---

