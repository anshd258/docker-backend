from cabin.models.property import Property
from cabin.models.property_reviews import PropertyReview
from rest_framework import serializers
from cabin.models import *
from user.serializers import UserSerializer

class LocationSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()
    avg_price = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    meta_data=serializers.SerializerMethodField()
    class Meta:
        model = Location
        fields = ['id', 'name', 'description','avg_price', 'avg_rating', 'meta_data','location_address', 'photo', 'cabin_type','properties']
    def get_meta_data(self,obj):
        return LocationMetaDataSerializer(LocationMetaData.objects.filter(location=obj),many=True).data
    def get_properties(self, obj):
        filtered_properties = self.context.get('filtered_properties', [])
        print(filtered_properties)
        location_properties = [prop for prop in filtered_properties if prop.location == obj]
        print(location_properties)
        return PropertySerializer(location_properties, many=True).data
    def get_avg_price(self, obj):
        filtered_properties = self.context.get('filtered_properties', [])
        location_properties = [prop for prop in filtered_properties if prop.location == obj]
        return round(sum([prop.price for prop in location_properties]) / len(location_properties),-2)
    def get_avg_rating(self, obj):
        filtered_properties = self.context.get('filtered_properties', [])
        location_properties = [prop for prop in filtered_properties if prop.location == obj]
        return sum([prop.overallrating for prop in location_properties]) / len(location_properties)

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PropertyMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMetaData
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    amenities = serializers.SerializerMethodField()
    def get_amenities(self, obj):
        return PropertyMetaDataSerializer(PropertyMetaData.objects.filter(property=obj,key="amenities"),many=True).data
    class Meta:
        model = Property
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    property = PropertySerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Reservation
        fields = [field.name for field in Reservation._meta.fields]+['property','user']


class PaymentStatusSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentStatus
        fields = '__all__'

class LocationMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMetaData
        fields = '__all__'
   

class PropertyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyReview
        fields = '__all__'

class PropertyFullSerializer(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField()
    metadata=serializers.SerializerMethodField()
    rooms=serializers.SerializerMethodField()
    def get_rooms(self,obj):
        return RoomSerializer(Room.objects.filter(_property=obj),many=True).data
    def get_reviews(self,obj):
        return PropertyReviewSerializer(PropertyReview.objects.filter(property=obj),many=True).data
    def get_metadata(self,obj):
        return PropertyMetaDataSerializer(PropertyMetaData.objects.filter(property=obj),many=True).data
    class Meta:
        model = Property
        fields = [field.name for field in Property._meta.fields]+['reviews','metadata','rooms']

