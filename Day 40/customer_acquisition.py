import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/2468d5561b6b2cf2ba9d71ac482d2451/flightDeals/users'

fname = input('What is your First Name? \n')
lname = input('What is your Last Name? \n')
email = input('What is your email? \n')

query = {
    'user': {
        'firstName': fname,
        'lastName': lname,
        'email': input('Type your email again. \n'),
    }
}

response = requests.post(url= SHEETY_ENDPOINT, json=query)
if (response.status_code == 200):
    print("Success! Your email is added.")

