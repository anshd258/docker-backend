from django.views import View
from django.http import JsonResponse
from user.get_user import FindUser


class GetUser(View):

    def get(self, request):
        try:
            a = FindUser(request.GET["phone"])
            userdata = a.get_user()
            if userdata:
                request.session['userdata'] = userdata
                return JsonResponse(userdata)
            else:
                return JsonResponse({"status": "User Not Found"}, status=404)
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=404)

