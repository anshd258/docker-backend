from rest_framework import serializers
from service.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='item.name')
    desc = serializers.CharField(source='item.desc')

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
