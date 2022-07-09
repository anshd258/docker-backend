from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'
