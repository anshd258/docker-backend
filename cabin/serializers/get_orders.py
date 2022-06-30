from rest_framework import serializers
from django.contrib.auth.models import User
from cabin.models import Location, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'location_address']


class ReservationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Reservation
        fields = ['adults', 'price', 'location', 'children', 'checkin', 'checkout', 'rooms']
