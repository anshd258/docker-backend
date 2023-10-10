import json
from django.http import JsonResponse
from user.models.user_info import UserInfo
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class UpdateUser(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request):
        try:
            user=request.user
            u=UserInfo.objects.get(user=user)
            data=json.loads(request.body)
            for key,value in data.items():
                setattr(u,key,value)
            u.save()
            return JsonResponse({'status':'success'})
        except Exception as e:
            return JsonResponse({'status':'error','error':str(e)})