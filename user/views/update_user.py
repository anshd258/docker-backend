import json
from django.http import JsonResponse
from user.models.user_info import UserInfo
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

class UpdateUser(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            body = json.loads(request.body)
            user_obj = UserInfo.objects.filter(user=user).first()
            if user_obj is None:
                return JsonResponse({'status': 'User not found'}, status=400)
            for key, value in body.items():
                setattr(user_obj, key, value)
            user_obj.save()
            return JsonResponse({'status': 'User updated'}, status=200)
        else:
            return JsonResponse({'status': 'User not authenticated'}, status=401)