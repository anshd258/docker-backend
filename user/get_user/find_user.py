from user.models import UserInfo
from django.contrib.auth.models import User
from django.core import serializers
import json


class FindUser:
    def __init__(self,contact):
        self.__contact__ = contact

    def get_user(self):
        user = UserInfo.objects.filter(contact=self.__contact__).first()

        if user is None:
            return {"status": "A user with the given phone number do not exist."}

        user_obj = User.objects.filter(id=user.id).all()
        return {"status": json.loads(serializers.serialize(
            "json",
            user_obj,
            fields=('username', 'first_name', 'last_name', 'email')
        ))}
