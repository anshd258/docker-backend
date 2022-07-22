from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem
from django.db.models import Q
from user.models import UserInfo


def get(request):
    try:
        order_dict = {"status": "error"}
        orders = []

        if request.GET.get("order_id"):
            order_id = request.GET["order_id"]
            order = Order.objects.filter(pk=order_id).first()
            order_items = OrderItem.objects.filter(order=order).exclude(total=0)
            order_dict = OrderSerializer(order).data
            order_dict['items'] = OrderItemSerializer(order_items, many=True).data

        elif request.user:
            orders = Order.objects.filter(user=request.user).all()

        elif request.GET.get("user_id"):
            orders = Order.objects.filter(user_id=request.GET["user_id"]).all()

        elif request.GET.get("contact"):
            user = UserInfo.objects.filter(contact=request.GET["contact"]).first().user
            orders = Order.objects.filter(user=user).all()

        elif request.GET.get("location_id"):
            orders = Order.objects.filter(location_id=request.GET["location_id"]).all()

        # collecting order items for each order
        if not request.GET.get("order_id"):
            order_dict = OrderSerializer(orders, many=True).data
            i = 0
            for order in orders:
                order_item = OrderItem.objects.filter(order=order).exclude(total=0).all()
                order_dict[i]['items'] = OrderItemSerializer(order_item, many=True).data
                i += 1

        order_dict = {
            'order': order_dict
        }
        return JsonResponse(order_dict)

    except Exception as e:
        return JsonResponse({"status": str(e)}, status=404)


class FindOrders(View):
    pass
