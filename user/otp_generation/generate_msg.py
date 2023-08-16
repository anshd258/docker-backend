import requests
from django.conf import settings
from datetime import datetime, timedelta
import json
from requests import post, Response
from requests.auth import HTTPBasicAuth
import urllib.parse
# referred from https://docs.fast2sms.com/#otp-sms-api

class GenerateMsg:
    wati_base_url = "https://test-server-9620.wati.io"
    wati_url_route = "/api/v1/sendSessionMessage/"
    access_token = "Bearer <TOKEN>"
    headers = {"Authorization": access_token}
    def __init__(self,contact=None, msg=None):
        self.__contact__ = contact
        self.__response__ = None
        self.__msg__ = msg
    def set_contact(self, contact):
        self.__contact__ = contact

    def send_message(self):
        message = self.__msg__
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
        print(body)
        response = requests.post(url=url, data=body, headers=headers)
        print(response.content)
        self.__response__ = response

    def send_wati_message(self):
        url = self.wati_base_url + self.wati_url_route
        body = {
            "phone": self.__contact__,
            "message": self.__msg__,
            "type": "text"
        }
        response = requests.post(url=url, data=body, headers=self.headers)
        print(response.content)
        self.__response__ = response
        wati_endpoint = self.wati_base_url + self.wati_url_route + \
                        self.__contact__+ "?messageText=" + \
                        urllib.parse.quote_plus(self.__msg__)
        response: Response = post(
                    url=wati_endpoint, data={}, headers=self.headers)