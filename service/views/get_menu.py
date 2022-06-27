from django.http import JsonResponse
from django.views import View
from service.catalog import GenerateCatalog


class GetMenu(View):
<<<<<<< HEAD
    def get(self, request):
        try:
            request.GET["location"]
        except:
            return JsonResponse({"status": "Please Enter a valid location"})
        catalog = GenerateCatalog()
        return JsonResponse({"catalog": catalog.build_catalog(request.GET["location"])})
=======
    def get(self, request) -> JsonResponse:
        catalog = GenerateCatalog()
        try:
            return JsonResponse({"catalog": catalog.build_catalog(request.GET['location'])})
        except Exception as e:
            return JsonResponse({"error": str(e)})
>>>>>>> e4ccabad07f38f7685912cde539a6e4997f984e7

    def post(self):
        pass
