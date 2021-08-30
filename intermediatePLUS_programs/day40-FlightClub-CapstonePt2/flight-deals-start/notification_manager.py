# references: https://www.twilio.com/docs/sms/quickstart/python

from twilio.rest import Client

TWILIO_SID =  "My Twilio SID"
TWILIO_AUTH_TOKEN = "My Twilio Auth Token"
TWILIO_VIRTUAL_NUMBER = "My Twilio Virtual #"
TWILIO_VERIFIED_NUMBER = "My Twilio Verified #"


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


