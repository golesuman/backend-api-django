from rest_framework import views, permissions, response
from ecommerce.serializers.cart_serializer import CartItemSerializer
from ecommerce.models.cart import CartItem


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
