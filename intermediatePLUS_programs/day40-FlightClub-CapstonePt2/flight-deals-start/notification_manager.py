# references: https://www.twilio.com/docs/sms/quickstart/python
import smtplib

from twilio.rest import Client

TWILIO_SID = "My Twilio SID"
TWILIO_AUTH_TOKEN = "My Twilio Auth Token"
TWILIO_VIRTUAL_NUMBER = "My Twilio Virtual #"
TWILIO_VERIFIED_NUMBER = "My Twilio Verified #"

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

MY_EMAIL = "hidden for this module"
MY_PASSWORD = "hidden for this module"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN) # initialize client object with SID & Auth Token

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid) # print if successfully sent

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
