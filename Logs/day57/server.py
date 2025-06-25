from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)


@app.route('/')
def home_page():
    random_number = random.randint(0,10)
    current_date = date.today()
    current_year = current_date.year
    return render_template("index.html" , num = random_number , year = current_year)


if __name__ == "__main__":
    app.run(port=8080, debug=True)