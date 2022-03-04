from datetime import datetime
import requests

USERNAME = 'animagus'
TOKEN = 'awdadafafaefaw'

pixela_endpoint = 'https://pixe.la/v1/users'

user_parameter = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url = pixela_endpoint, json= user_parameter)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_parameters = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url= graph_endpoint, json=graph_parameters, headers= headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{graph_parameters['id']}"

today = datetime.now()

add_pixel_parameters = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input("How many Km did you cycle today?"),
}

response = requests.post(url= add_pixel_endpoint, json=add_pixel_parameters, headers= headers)
print(response.text)

update_endpoint = f"{add_pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_parameter = {
    'quantity': '15'
}

# response = requests.put(url= update_endpoint, json=update_parameter, headers= headers)
# print(response.text)

delete_endpoint = f"{add_pixel_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url= delete_endpoint, headers= headers)
# print(response.text)