from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

# CREATE DATABASE
db = sqlite3.connect("books.db", check_same_thread=False)
cursor = db.cursor()

# # CREATE TABLE
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


@app.route('/')
def home():
    all_books = cursor.execute("SELECT * from books")
    books = list(all_books)
    return render_template('index.html', books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        cursor.execute(
            "INSERT INTO books VALUES(NULL, ?, ?, ?)", (name, author, rating))
        db.commit()

        return redirect(url_for("home"))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        print(book_id)
    #     book_to_update = books.get(book_id)
    #     book_to_update.rating = request.form["rating"]
    #     db.session.commit()
    #     return redirect(url_for('home'))
    # book_id = request.args.get('id')
    # book_selected = Book.query.get(book_id)
    return render_template("edit.html")
    pass

if __name__ == "__main__":
    app.run(debug=True)
