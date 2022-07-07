from django.views import View
from django.http import JsonResponse
from user.get_user import FindUser


class GetUser(View):

    def get(self, request):
        try:
            a = FindUser(request.GET["phone"])
        except:
            return JsonResponse({"Error": "Invalid Arguments"})

        return JsonResponse(a.get_user())

    def post(self):
        pass
