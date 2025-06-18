
# 📅 Day 54 - Flask Web Development (Calculator API)

This project from **Day 54** of the [100 Days of Code: Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) demonstrates how to create a simple RESTful API using **Flask**.

---

##  Project Overview

We create a minimal API that supports:

- URL-based endpoints for math operations
- Query parameter parsing via `request.args`
- Returning calculated results in plain text

---

## 🧾 Code Breakdown

### `main.py`

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API! Use /add, /subtract, /multiply, or /divide with query parameters ?a= and ?b="

@app.route('/add')
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return str(a + b)

@app.route('/subtract')
def subtract():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return str(a - b)

@app.route('/multiply')
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return str(a * b)

@app.route('/divide')
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    if b == 0:
        return "Error: Division by zero is not allowed."
    return str(a / b)

if __name__ == "__main__":
    app.run(debug=True)
````

---

## 🚀 How to Use

1. **Clone the repo**:

   ```bash
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day54
   ```

2. **Install Flask**:

   ```bash
   pip install flask
   ```

3. **Run the server**:

   ```bash
   python main.py
   ```

4. **Access API Endpoints** in your browser or tools like Postman:

   * `http://127.0.0.1:5000/add?a=10&b=5` → `15.0`
   * `http://127.0.0.1:5000/subtract?a=10&b=5` → `5.0`
   * `http://127.0.0.1:5000/multiply?a=10&b=5` → `50.0`
   * `http://127.0.0.1:5000/divide?a=10&b=2` → `5.0`

---

## 📦 Dependencies

* Python 3.x
* Flask

To install:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
flask
```

---

## 🔖 Concepts Covered

* Flask routing
* Query parameters (`request.args`)
* REST principles
* Error handling (division by zero)

---

## 🎓 Source

Course: [100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)
Repo: [@2tzz](https://github.com/2tzz/100Days_Python_Udemy)

---

