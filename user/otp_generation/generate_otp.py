import random
import jwt
import requests


class GenerateOTP:

    def __init__(self):
        self.__contact__ = None
        self.__otp__ = None
        self.__token__ = None
        self.__response__ = None

    def set_contact(self, contact):
        self.__contact__ = contact

    def send_message(self):
        url = 'https://www.fast2sms.com/dev/bulkV2'
        message = f'The OTP for login is {self.__otp__}'
        headers = {
            "authorization": "vjhrIsz40e9CPGQmT7ldFw5OaRb3fxnpSgXBJVAiH8qyZtuLUEQUx9SanhRLKj7oGpq6lFdJ5wZ2XCg8",
            "Content-Type": "application/json"
        }
        body = {
            "route": "v3",
            "sender_id": "FTWSMS",
            "message": message,
            "language": "english",
            "flash": 0,
            "numbers": self.__contact__,
        }
        response = requests.request("POST", url=url, data=body, headers=headers)
        print(response)
        self.__response__ = response

    def otp_generate(self):
        s = ""
        for i in range(6):
            s += str(random.randint(0, 9))
        self.__otp__ = s

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
