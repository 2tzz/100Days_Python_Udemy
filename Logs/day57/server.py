from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    random_number = random.randint(0,10)
    current_date = date.today()
    current_year = current_date.year
    return render_template("index.html" , num = random_number , year = current_year)


@app.route('/guess/<sample_name>')
def guess_page(sample_name):
    response = requests.get(url=f"https://api.agify.io/?name={sample_name}" )
    response.raise_for_status()
    data = response.json()
    guessing_age = data['age']

    response_gender = requests.get(url=f"https://api.genderize.io?name={sample_name}" )
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    gender = data_gender['gender']

    return render_template("guess.html" , name = sample_name , age = guessing_age , gender = gender)


if __name__ == "__main__":
    app.run(port=8080, debug=True)