from django.views import View
from django.http import JsonResponse
from user.get_user import FindUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class GetUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = FindUser(request.user)
        return JsonResponse(user.get_user(), safe=False)
    def post(self):
        pass
