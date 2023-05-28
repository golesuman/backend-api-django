from rest_framework import views, status, serializers, permissions, response
from ecommerce.serializers.order_serializer import OrderItemSerializer, OrderSerializer
from ecommerce.models.order import Order, OrderItem


class OrderCreateAndListView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = OrderItem.objects.filter(order__user=request.user)
        serializer = OrderItemSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(request.data)
        serializer.save()
        return response.Response(serializer.data)
