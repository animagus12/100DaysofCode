from turtle import pos
import requests
from flask import Flask, render_template

app = Flask(__name__)

BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
responses = requests.get(BLOG_URL).json()


@app.route('/')
def home():
    return render_template('index.html', all_posts = responses)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post(index):
    response = None
    for response in responses:
        if response["id"] == index:
            requested_post = response
    return render_template("post.html", post = requested_post)


if __name__ == "__main__":
    app.run(debug=True)
