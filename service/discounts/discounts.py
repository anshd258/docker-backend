from ..models import OrderItem,Discount


def Discounts(order_id,apply):

    order_items = OrderItem.objects.filter(order_id=order_id).all()
    discounts_available = []
    recommended = []

    for order_item in order_items:
        min_price = order_item.listed_price
        coupon_name = ""
        discounts = Discount.objects.filter(to_item=order_item.item).all()

        for discount in discounts:
            if discount.min_price <= order_item.listed_price:
                temp_price = order_item.listed_price - min(order_item.listed_price * discount.percent / 100, discount.upto)
                discounts_available.append(
                    {
                        "discount_id": discount.id,
                        "item_id": order_item.item_id,
                        "item_name": order_item.item.name,
                        "final_price": temp_price,
                        "listed_price": order_item.listed_price,
                        "cutoff": discount.percent,
                        "upto": discount.upto,
                    }
                )

                if temp_price < min_price:
                    order_item.discount = discount.percent
                    coupon_name = discount.code

        if apply:
            order_item.save()
        else:
            recommended.append(
                {
                    "item_name": order_item.item.name,
                    "coupon_name": coupon_name,
                }
            )
            
    if apply:
        return {"discounts": discounts_available}
    else:
        return {"discounts": discounts_available, "recommended": recommended}