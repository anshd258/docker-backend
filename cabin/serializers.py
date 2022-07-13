from rest_framework import serializers
from cabin.models import Location, Reservation, PaymentStatus
from user.serializers import UserInfoSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'location_address']


class ReservationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)
    user = UserInfoSerializer(many=False, read_only=True)

    class Meta:
        model = Reservation
        fields = ['adults', 'price', 'user', 'location', 'children', 'checkin', 'checkout', 'rooms']


class PaymentStatusSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentStatus
        fields = '__all__'
        fields = ['payment_ref_id', 'status', 'reservation', 'amount', 'create_time', 'update_time']
