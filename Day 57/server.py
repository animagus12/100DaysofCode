from unicodedata import name
from urllib import response
from flask import Flask, render_template, request
import random
from datetime import date
import requests

app = Flask(__name__)

GENDERIZE = 'https://api.genderize.io'

AGIFY = 'https://api.agify.io'

BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'

now = date.today().year


@app.route('/')
def home():
    rng = random.randint(1, 10)
    return render_template('index.html', num=rng, year=now)


@app.route('/guess/<name>')
def guess(name):
    genderize_params = {
        'name': name
    }
    agify_params = {
        'name': name
    }
    gender_response = requests.get(GENDERIZE, params=genderize_params)
    age_response = requests.get(AGIFY, params=agify_params)
    return render_template('guesser.html', gender=gender_response.json()["gender"], age=age_response.json()["age"], year=now, name=name)

@app.route('/blog')
def blog():
    response = requests.get(BLOG_URL)
    return render_template("blog.html", posts = response.json())

if __name__ == "__main__":
    app.run(debug=True)
