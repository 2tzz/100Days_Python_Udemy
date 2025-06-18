
# 📅 Day 55 - Flask Web Development (Higher or Lower Game)

Welcome to **Day 55** of the [100 Days of Python - Udemy Course](https://www.udemy.com/course/100-days-of-code/).  
This day's project focuses on building a **Flask Web App** for a "Higher or Lower" guessing game.

## 🚀 What You’ll Learn

- Basics of Flask
- How to serve HTML content via Flask
- URL routing
- Using decorators and random numbers in web apps

---

## 🧠 Project Overview

We built a simple web app that:

- Randomly selects a number between 0 and 9 at the start.
- When the user enters a number in the URL (e.g. `/5`), it checks if it matches the hidden number.
- Responds with a visual message saying "Too high", "Too low", or "Correct".

---

## 🧾 Code Breakdown

### `main.py`

```python
from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)
print(f"Random number is: {number}")

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess > number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)
````

---

## 🧪 How to Run the App

1. Clone this repo:

   ```bash
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day55
   ```

2. Install Flask:

   ```bash
   pip install flask
   ```

3. Run the script:

   ```bash
   python main.py
   ```

4. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and try different numbers in the URL, like:

   ```
   http://127.0.0.1:5000/3
   ```

---

## 🖼️ GIF Preview

You’ll see a fun GIF response for each guess to make it more engaging!

---

## 📦 Dependencies

* Python 3.x
* Flask

Install them via:

```bash
pip install -r requirements.txt
```

(You can create a `requirements.txt` with just `flask` in it.)

---

## 📚 Related Topics

* Flask Basics
* Web Development with Python
* HTTP Routing

---

## 🔖 Credits

Course: [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
Author of Code: [@2tzz](https://github.com/2tzz)

---

```
