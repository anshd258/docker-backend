from django.views import View
from django.http import JsonResponse
from user.get_user import FindUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import UserInfo
from user.serializers import UserInfoSerializer
class GetUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        u=UserInfo.objects.get(user=user)
        userdata=UserInfoSerializer(u).data
        return JsonResponse({'userdata':userdata})
    def post(self):
        pass
