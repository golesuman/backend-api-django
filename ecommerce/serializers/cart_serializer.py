from rest_framework import serializers

from ecommerce.models.cart import Cart, CartItem
from ecommerce.serializers.product_serializer import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(serializers.Serializer):
    id = serializers.CharField()
    cart = serializers.CharField()
    product = ProductSerializer()
