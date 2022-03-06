import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/2468d5561b6b2cf2ba9d71ac482d2451/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_flights(self):
        sheety_get = SHEETY_PRICES_ENDPOINT
        self.response = requests.get(sheety_get)
        return self.response.json()['prices']

    def update_flights(self, row, new_data):
        sheety_update = f'{SHEETY_PRICES_ENDPOINT}/{row}'
        updated_data = {
            'price': {
                'iataCode': new_data
            }
        }
        self.response = requests.put(url=sheety_update, json=updated_data)
        print(self.response.text)
