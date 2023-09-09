from rest_framework import serializers
from service.models import *
from user.serializers import UserInfoSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LocationAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['address']

class ProviderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='item.name')
    desc = serializers.CharField(source='item.desc')
    provider_id = serializers.IntegerField(source='item.provider.id')
    provider_name = serializers.CharField(source='item.provider.business_name')

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    location=LocationAddressSerializer()
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class RentalBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalBooking
        fields = '__all__'