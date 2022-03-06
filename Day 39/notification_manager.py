from twilio.rest import Client

TWILIO_SID = 'AC8a2f8b00db295548bc94aa23a7ffe34b'
TWILIO_AUTH_TOKEN = '8627c570ceab4fcb41d418b276f90af4'
TWILIO_VIRTUAL_NUMBER = '+19107271760'
TWILIO_VERIFIED_NUMBER = '+919090305392'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
        # Prints if successfully sent.
        print(message.sid)
