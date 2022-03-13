import requests
from twilio.rest import Client

ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'f6c1586d81afb95c234599cc660f643b'

account_sid = 'AC8a2f8b00db295548bc94aa23a7ffe34b'
auth_token = '18d7bdd8b8ca3b9a461a57e7e395aba0'

parameters = {
    'lat': -22.560881, 
    # -19.433442,
    # 22.260424,
    'lon': 17.065756,
    # 121.626892,
    # 84.853584,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()

will_rain = False

for i in range(0, 12):
    weather_data = response.json()['hourly'][i]['weather'][0]['id']
    if weather_data < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring your Umbrella!",
                        from_='+19107271760',
                        to='+919090305392'
                    )

    print(message.status)
