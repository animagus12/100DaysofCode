import requests
from  datetime import datetime

GENDER = 'male'
WEIGHT_KG = '100'
HEIGHT_CM = '180'
AGE = '20'

NUTRITIONIX_APP_ID = '1085f87d'
NUTRITIONIX_API_KEY = 'ce3141f2490dc943a63e318cbcdcd3fa'

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/2468d5561b6b2cf2ba9d71ac482d2451/myWorkouts/workouts'

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
response.raise_for_status()

today = datetime.now()

for workout in response.json()['exercises']:
    workout_parameters = {
        'workout': {
            'date': today.strftime("%d/%m/%Y"),
            'time': today.strftime("%X"),
            'exercise': workout['name'].title(),
            'duration': workout['duration_min'],
            'calories': workout['nf_calories'],
        }
    }

    ## No Auth
    # sheety_response = requests.post(url=sheety_endpoint, json=workout_parameters)
   
    ## Bearer Token
    bearer_headers = {
    'Authorization': 'Bearer tvserbtesrersbtservtrestseybesybsybysr43',
    }
    sheety_response = requests.post(url=sheety_endpoint, json=workout_parameters, headers=bearer_headers)
