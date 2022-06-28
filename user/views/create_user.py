from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from user.models import UserInfo
from user.get_user import FindUser


class CreateUser(View):
    def get(self):
        pass

    def post(self, request):
        user = User.objects.create(
            username=request.POST["username"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            password=make_password(request.POST["password"]),
            email=request.POST["email"],
        )
        user_details = UserInfo.objects.create(
            user_id=user.id,
            contact=request.POST["contact"],
        )
        A = FindUser(request.POST["contact"])
        return JsonResponse(A.get_user())
