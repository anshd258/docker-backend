import random
import jwt
import requests
from django.conf import settings
# referred from https://docs.fast2sms.com/#otp-sms-api

class GenerateOTP:

    def __init__(self):
        self.__contact__ = None
        self.__otp__ = None
        self.__token__ = None
        self.__response__ = None
        self.__message__ = None
    def set_contact(self, contact):
        self.__contact__ = contact
    def set_message(self, message):
        self.__message__ = message
    def send_message(self):
        message = "Please use this OTP " + self.__otp__ + " to login to Brisphere"
        if self.__message__ is not None: message=self.__message__
        url = settings.FAST2SMS_API_ENDPOINT
        headers = {
            "Authorization":  settings.FAST2SMS_API_KEY
        }
        body = {
            "route": "q",
            "message": message,
            "language": "english",
            "numbers": self.__contact__,
        }
        response = requests.post(url=url, data=body, headers=headers)
        print(response)
        self.__response__ = response

    def otp_generate(self):
        s = ""
        for i in range(6):
            s += str(random.randint(0, 9))
        self.__otp__ = s
        return s
    def jwt_token(self):
        payload_data = {
            "otp": self.__otp__,
        }
        my_secret = 'brisphere'
        token = jwt.encode(
            payload=payload_data,
            key=my_secret
        )
        self.__token__ = token

    def get_otp(self, contact):
        self.set_contact(contact)
        self.otp_generate()
        self.jwt_token()
        self.send_message()
        return {"token": self.__token__, }
