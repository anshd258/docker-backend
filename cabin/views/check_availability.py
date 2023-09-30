from django.http import JsonResponse
from django.views import View
from cabin.availability.calculate_availability import CalculateAvailability
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.authentication.secretkeyauth import SecretKeyAuthentication, SecretKeyPermission
class CheckAvailability(APIView):
    authentication_classes = [SecretKeyAuthentication]
    permission_classes = [SecretKeyPermission]
    def get(self, request):
        try:
            return JsonResponse({"status": CalculateAvailability(
                request.GET['id'],
                request.GET['rooms'],
                request.GET['checkin'],
                request.GET['checkout']
            )})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self):
        pass