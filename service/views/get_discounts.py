from django.http import JsonResponse
from django.views import View
from ..models import *


class GetDiscount(View):
    def get(self, request):
        order_id = request.GET["order_id"]
        order_items = OrderItem.objects.filter(order_id=order_id).all()
        discounts_available = []
        recommended = []
        for each in order_items:
            min_price = each.listed_price
            name = ""
            discounts = Discount.objects.filter(to_item=each.item).all()
            for one in discounts:
                if one.min_price <= each.listed_price:
                    temp_price = each.listed_price - min(each.listed_price * one.percent / 100, one.upto)
                    discounts_available.append(
                        {
                            "discount_id": one.id,
                            "item_id": each.item_id,
                            "item_name": each.item.name,
                            "final_price": temp_price,
                            "listed_price": each.listed_price,
                            "cutoff": one.percent,
                            "upto": one.upto,
                        }
                    )
                    if temp_price < min_price:
                        each.discount = one.percent
                        name = one.code
            recommended.append(
                {
                    "item_name": each.item.name,
                    "coupon_name": name,
                }
            )
        return JsonResponse({"discounts": discounts_available , "recommended": recommended})
