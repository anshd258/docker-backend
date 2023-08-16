from service.serializers import OrderSerializer
from .models import *
from rest_framework import serializers
from user.serializers import UserInfoSerializer



class WorkerSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(read_only=True)

    class Meta:
        model = Worker
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    order=OrderSerializer()
    worker=WorkerSerializer()
    class Meta:
        model = Job
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = '__all__'