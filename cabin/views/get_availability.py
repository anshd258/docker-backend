import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
import pytz
from cabin.models import Property
from cabin.models.location import Location
from cabin.models.payment_status import PaymentStatus
from cabin.models.reservation import Reservation
from cabin.availability import calculate_availability
from cabin.serializers import LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from user.authentication.secretkeyauth import SecretKeyAuthentication, SecretKeyPermission
class GetAvailability(APIView):
    authentication_classes = [SecretKeyAuthentication]
    permission_classes = [SecretKeyPermission]
    def get(self,request):
        try:
            properties=Property.objects.all()
            locations={}
            fromdate=pytz.utc.localize(datetime.datetime.strptime(request.GET.get('fromdate'), '%Y-%m-%dT%H:%M:%S.%f'))
            todate=pytz.utc.localize(datetime.datetime.strptime(request.GET.get('todate'), '%Y-%m-%dT%H:%M:%S.%f'))
            for i in properties:
                if calculate_availability.CalculateAvailability(i.id,request.GET.get('rooms'),fromdate,todate):
                    print('herer')
                    if i.location not in locations:
                        locations[i.location]=[]
                    locations[i.location].append(i)
            response=[]
            print(locations)
            for i in locations:
                l=LocationSerializer(i,context={'filtered_properties':locations[i]},many=False).data
                response.append(l)
            return JsonResponse(response,safe=False,status=200)
        except Exception as e:  
            print(e)
            return JsonResponse({'status':'error'},status=400)
    def post(self,request):
        pass
