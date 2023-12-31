import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from service.serializers import RentalBookingSerializer
from ..models import RentalBooking, Rental
from user.models import UserInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateRentalBooking(request):
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            user=request.user
            user=get_object_or_404(UserInfo,user=user)
            rental_id=body['rental_id']
            rental=get_object_or_404(Rental,pk=rental_id)
            start_location=body['start_location']
            end_location=body['end_location']
            start_coordinates=body['start_coordinates']
            end_coordinates=body['end_coordinates']
            rental_booking=RentalBooking.objects.create(user=user,rental=rental,start_location=start_location,end_location=end_location,start_coordinates=start_coordinates,end_coordinates=end_coordinates)
            rental_booking.save()
            return JsonResponse({'rental_booking':RentalBookingSerializer(rental_booking).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)