from rest_framework import serializers
from service.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'address']


class ProviderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'location', 'business_name', 'provider_name']


class ItemSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
