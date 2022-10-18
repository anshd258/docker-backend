from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from service.models import Location


class Checkin(View):
    def get(self, request):
        try:
            location = Location.objects.get(name=request.GET["location"])
            user_id = request.session.get('userdata', {}).get('user', {}).get('id', None)
            if not user_id:
                user_id = request.GET["user_id"]
            no_of_persons = int(request.GET["persons"])
            location.check_in(no_of_persons)
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
