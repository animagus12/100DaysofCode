from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/update")
def update():
    return render_template("edit.html")

@app.route("/delete")
def delete():
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
