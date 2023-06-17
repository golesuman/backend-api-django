from django.contrib.auth.models import User
from rest_framework import permissions, response, status, views

from ecommerce.models.cart import Cart, CartItem
from ecommerce.serializers.cart_serializer import CartItemSerializer


class CartCreateAndListAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(cart__user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return response.Response(serializer.data)

    def post(self, request, product_id, *args, **kwargs):
        user = User.objects.get(id=1)
        # user = request.user
        quantity = request.data.get("quantity")
        cart, created = Cart.objects.get_or_create(user=user)
        item = CartItem.objects.create(cart=cart, product_id=product_id)
        serializer = CartItemSerializer(item)
        return response.Response(serializer.data)


class CartRetrieveUpdateDeleteAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, cart_id, *args, **kwargs):
        cart_item = Cart(id=cart_id)
        cart_item.is_deleted = True
        cart_item.save()

        return response.Response("Deleted Successfully", status=status.HTTP_200_Ok)
