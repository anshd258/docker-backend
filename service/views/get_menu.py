from django.http import JsonResponse
from django.views import View
from service.catalog import GenerateCatalog


class GetMenu(View):
    def get(self, request):
        try:
            request.GET["location"]
        except:
            return JsonResponse({"status": "Please Enter a valid location"})
        catalog = GenerateCatalog()
        return JsonResponse({"catalog": catalog.build_catalog(request.GET["location"])})

    def post(self):
        pass
