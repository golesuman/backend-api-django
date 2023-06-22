from rest_framework import serializers

from ecommerce.models.order import Order, OrderItem
from ecommerce.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.Serializer):
    order = OrderSerializer()
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    price = serializers.CharField()
    # class Meta:
    #     model = OrderItem
    #     fields = "__all__"
