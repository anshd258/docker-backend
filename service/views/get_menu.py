from django.http import JsonResponse
from django.views import View
from service.catalog import GenerateCatalog


class GetMenu(View):
    def get(self, request) -> JsonResponse:
        catalog = GenerateCatalog()
        try:
            return JsonResponse({"catalog": catalog.build_catalog(request.GET['location'])})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    def post(self):
        pass
