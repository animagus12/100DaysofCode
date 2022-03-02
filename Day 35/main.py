import requests

ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = "f6c1586d81afb95c234599cc660f643b"
parameters = {
    "lat": 22.260424,
    "lon": 84.853584,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(
    url=ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)
