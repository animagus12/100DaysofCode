# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# longitude = response.json()['iss_position']['longitude']
# latitude =response.json()['iss_position']['latitude']

# iss_pos = (longitude, latitude)

# print(iss_pos)

import requests
from datetime import datetime

MY_LAT = 22.260424
MY_LONG = 84.853584

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params= parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)