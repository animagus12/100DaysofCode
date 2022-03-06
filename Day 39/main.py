# This file will need to use the DataManager,FlightSearch, FlightData, 
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_flights()

for data in sheet_data:
    if data['iataCode'] == '':
        code = flight_search.search(data['city'])
        data_manager.update_flights(data['id'], code)

    flights = flight_search.get_deals(data['iataCode'])
    
    if flights is None:
        continue
    elif flights.price <= data['lowestPrice']: 
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flights.price} to fly from {flights.origin_city}-{flights.origin_airport} to {flights.destination_city}-{flights.destination_airport}, from {flights.out_date} to {flights.return_date}."
        )
        