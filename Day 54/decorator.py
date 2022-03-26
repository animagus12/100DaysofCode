# Decorator

import time


def delay_decorator(function):
    def wrapper_fnc():
        time.sleep(2)
        # Do something before the function
        function()
        # function()
        # Do something after the function
    return wrapper_fnc


@delay_decorator
def say_hello():
    print("Hello!")


@delay_decorator
def say_bye():
    print("Bye")

# @delay_decorator
def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()
