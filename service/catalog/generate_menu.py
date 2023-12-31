from ..models import ServiceArea, Provider, FoodItem, Location
from ..serializers import FoodItemSerializer


class GenerateCatalog:
    def __init__(self):
        self.__location__ = None
        self.__providers__ = None
        self.__catalog__ = None

    def set_location(self, location):
        try:
            self.__location__ = Location.objects.get(name=location)
        except:
            pass

    def get_providers(self):
        self.__providers__ = ServiceArea.objects.filter(location=self.__location__).values('provider')

    def get_catalog(self):
        self.__catalog__ = FoodItem.objects.filter(provider__in=self.__providers__).all()

    def calculate_surge(self):
        def surge(item):
            item['final_price'] = item['price'] * self.__location__.surge
            if item['options']:
                [item['options'].update({option: price * self.__location__.surge})
                 for option, price in item['options'].items()]
            return item
        self.__catalog__ = list(map(surge, self.__catalog__.values()))

    def build_catalog(self, location):
        self.set_location(location)
        if not self.__location__:
            return {"status": "Enter a valid location"}
        self.get_providers()
        self.get_catalog()
        self.calculate_surge()
        return self.__catalog__

