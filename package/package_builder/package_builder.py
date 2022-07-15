from package.models import PackageItem
import math


class PackageBuilder:
    def __init__(self, duration, guests, preferences):
        self.duration = duration
        self.preferences = preferences
        self.guests = guests

    def calculate(self):
        total_duration = 0
        current_priority = 1
        package_price = 0
        itinerary = {}

        for each in self.preferences.split(','):
            package = PackageItem.objects.filter(id=each).first()
            total_duration += package.duration
            package_price += math.ceil(self.guests / package.max_guests) * package.sales_price
            itinerary[package.package_item] = math.ceil(self.guests / package.max_guests) * package.sales_price

        while current_priority <= 3:
            for each in PackageItem.objects.filter(priority=current_priority):
                total_duration += each.duration
                price = math.ceil(self.guests / each.max_guests) * each.sales_price
                if total_duration > self.duration:
                    if current_priority == 1:
                        return {"status": "The package can not be generated."}
                    else:
                        current_priority = 4
                        break
                package_price += price
                itinerary[each.package_item] = price
            current_priority += 1

        return {"itinerary": itinerary, 'package_price': package_price}
