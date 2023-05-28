from rest_framework import views, permissions, response, status
from ecommerce.serializers.cart_serializer import CartItemSerializer
from ecommerce.models.cart import Cart, CartItem


class CartCreateAndListAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(cart__user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CartItemSerializer(request.data)
        serializer.save()
        return response.Response(serializer.data)


class CartRetrieveUpdateDeleteAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, cart_id, *args, **kwargs):
        cart_item = Cart(id=cart_id)
        cart_item.is_deleted = True
        cart_item.save()

        return response.Response("Deleted Successfully", status=status.HTTP_200_Ok)
