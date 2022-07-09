from user.models import UserInfo
from django.contrib.auth.models import User
from ..serializers import UserInfoSerializer
import json


class FindUser:
    def __init__(self,contact):
        self.__contact__ = contact

    def get_user(self):
        user = UserInfo.objects.filter(contact=self.__contact__).first()
        return UserInfoSerializer(user).data
