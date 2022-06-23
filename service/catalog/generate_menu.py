from ..models import ServiceArea, Provider, Item, Location


class GenerateCatalog:
    def __init__(self):
        self.__location__ = None
        self.__providers__ = None
        self.__catalog__ = None

    def set_location(self, location):
        self.__location__ = Location.objects.get(name=location)

    def get_providers(self):
        self.__providers__ = ServiceArea.objects.filter(location=self.__location__).values('provider')

    def get_catalog(self):
        self.__catalog__ = Item.objects.filter(provider__in=self.__providers__)

    def calculate_surge(self):
        def surge(item):
            item['final_price'] = item['price'] * self.__location__.surge
            [item['options'].update({option: price * self.__location__.surge})
             for option, price in item['options'].items()]
            return item

        self.__catalog__ = list(map(surge, self.__catalog__.values()))

    def build_catalog(self, location):
        self.set_location(location)
        self.get_providers()
        self.get_catalog()
        self.calculate_surge()
        return self.__catalog__

