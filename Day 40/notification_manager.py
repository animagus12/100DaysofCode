import smtplib
from twilio.rest import Client

TWILIO_SID = 'AC8a2f8b00db295548bc94aa23a7ffe34b'
TWILIO_AUTH_TOKEN = '18d7bdd8b8ca3b9a461a57e7e395aba0'
TWILIO_VIRTUAL_NUMBER = '+19107271760'
TWILIO_VERIFIED_NUMBER = '+919090305392'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = 'neongen18@gmail.com'
MY_PASSWORD = 'Sbp@2001'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )