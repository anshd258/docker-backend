from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from user.models import UserInfo
from ..serializers import UserInfoSerializer
from rest_framework.authtoken.models import Token
from user.get_user import FindUser
import json


class CreateUser(View):

    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.create(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                password=make_password(data["password"]),
                email=data["email"],
            )
            user_details = UserInfo.objects.create(
                user_id=user.id,
                contact=data["contact"],
            )
            data = UserInfoSerializer(user_details, many=False).data
            token = Token.objects.get(user=user).key
            data["token"] = token

            return JsonResponse({"user": data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
