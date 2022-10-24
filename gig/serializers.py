from .models import *
from rest_framework import serializers
from user.serializers import UserInfoSerializer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(read_only=True)

    class Meta:
        model = Worker
        fields = '__all__'
