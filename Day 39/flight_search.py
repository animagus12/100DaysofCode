import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API = 'SGx2FYoxAC0jEWrYuZF7MDLwyZpcEVks'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def search(self, city):
        header = {
            'apikey': TEQUILA_API
        }
        query = {
            'term': city,
            'location_types': 'city'
        }
        response = requests.get(url= f'{TEQUILA_ENDPOINT}/locations/query', params= query, headers= header)
        code = response.json()['locations'][0]['code']
        return code

    def get_deals(self, destination):
        from_date = (datetime.now()+ timedelta(days=1)).strftime("%d/%m/%Y")
        to_date = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")
        header = {
            'apikey': TEQUILA_API
        }
        query = {
            "fly_from": 'LON',
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url = f'{TEQUILA_ENDPOINT}/v2/search', params= query, headers= header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data