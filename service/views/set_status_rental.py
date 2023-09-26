import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import RentalBookingSerializer
from ..models import RentalBooking
from user.models import UserInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SetStatusRental(request):
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            rental_id=body['rentalbooking_id']
            status=body['status']
            rental=get_object_or_404(RentalBooking,pk=rental_id)
            rental.status=status
            rental.save()
            return JsonResponse({'rental':RentalBookingSerializer(rental).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)
    return JsonResponse({'error':'Invalid Request'},status=404)