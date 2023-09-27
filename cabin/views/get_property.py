from django.http import JsonResponse
from django.views import View
from cabin.models.property import Property
from cabin.serializers import PropertyFullSerializer, PropertySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView

class GetProperty(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            property=Property.objects.filter(id=request.GET.get('id')).first()
            serializer=PropertyFullSerializer(property)
            return JsonResponse(serializer.data,status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)