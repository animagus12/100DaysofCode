'''
# def greet(name):
#     print("Hello " + name)
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice today?")

# name = input("Enter Your Name: ")
# greet(name)
'''

# Funtion with more than 1 input
'''
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

name = input("Enter Your Name: ")
location = input("Enter Your Location: ")
greet_with(name, location)
'''

#Function with Keyword Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

name = input("Enter Your Name: ")
location = input("Enter Your Location: ")
greet_with(location = location, name = name)