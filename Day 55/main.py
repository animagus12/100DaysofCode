from flask import Flask

app = Flask(__name__)


# to make a text bold
def make_bold(function):
    def wrapper_fnc():
        return "<b>" + function() + "</b>"
    return wrapper_fnc

# to make a text italic


def make_empas(function):
    def wrapper_fnc():
        return "<em>" + function() + "</em>"
    return wrapper_fnc

# to make a text underlined


def make_underlined(function):
    def wrapper_fnc():
        return "<u>" + function() + "</u>"
    return wrapper_fnc


# Different routes using the app.route decorator
@app.route('/')
def hello_world():
    return "<h1> Hello World <h1>"


# Creating variable paths and converting the path to a specified data types
@app.route('/bye')
@make_bold
@make_empas
@make_underlined
def bye():
    return "Bye"


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)


