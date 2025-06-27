
# 📅 Day 56 - Flask with Jinja2 Templates

This project for **Day 56** of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) introduces rendering dynamic HTML content using **Jinja2 templating** in **Flask**.

---

## 🧠 What You’ll Learn

- How to serve HTML templates with Flask
- How to pass variables to HTML using Jinja2
- How to dynamically render user input via URL

---

## 📂 File Structure

```

day56/
├── main.py
└── templates/
└── index.html

````

---

## 🧾 Code Breakdown

### `main.py`

```python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, name="Thiyura")

if __name__ == "__main__":
    app.run(debug=True)
````

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Day 56 - Flask Templates</title>
</head>
<body>
    <h1>Hello, I'm {{ name }}!</h1>
    <p>&copy; {{ year }}</p>
</body>
</html>
```

---

## 🧪 How to Run the App

1. **Clone the repo**:

   ```bash
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day56
   ```

2. **Install Flask**:

   ```bash
   pip install flask
   ```

3. **Run the app**:

   ```bash
   python main.py
   ```

4. **Open in browser**:
   Visit `http://127.0.0.1:5000` to see the dynamic template in action.

---

## 🧩 Concepts Used

* Flask Routing
* `render_template()`
* HTML with Jinja2
* Using Python variables inside HTML

---

## 📦 Dependencies

* Python 3.x
* Flask

Install with:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
flask
```

---

## 📚 Source

Course: [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
Repo: [@2tzz](https://github.com/2tzz/100Days_Python_Udemy)

---

