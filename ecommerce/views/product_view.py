from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import permissions, response, serializers, status, views

from ecommerce.models.product import Product, WishList
from ecommerce.serializers.product_serializer import ProductSerializer


class ProductCreateListAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(request.data)
        serializer.save()
        return response.Response(serializer.data)


class SearchAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        search_text = self.request.GET.get("search_text")
        products = Product.objects.filter(
            Q(name__contains=search_text) | Q(description__contains=search_text)
        )
        serializer = ProductSerializer(products, many=True)
        return response.Response(serializer.data)


class ProductCreateDetailUpdateDeleteAPI(views.APIView):
    def get(self, request, product_id, *args, **kwargs):
        queryset = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(queryset)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class WishListAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        product = ProductSerializer()

    def get(self, request, *args, **kwargs):
        # please uncomment this after testing
        # user = request.user
        user = User.objects.get(id=1)
        queryset = WishList.objects.filter(user=user)
        serializer = self.OutputSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class WishListCreateAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        product = ProductSerializer()

    class InputSerializer(serializers.Serializer):
        product_id = serializers.CharField()

    def get_wishlist_of_user(self, user):
        return WishList.objects.filter(user=user)

    def post(self, request, product_id, *args, **kwargs):
        # uncomment it after testing
        # user = request.user
        user = User.objects.get(id=1)  # comment this after testing
        wish_list = WishList(user=user, product_id=product_id)
        wish_list.save()
        wish_list_for_user = self.get_wishlist_of_user(user)
        output_serializer = self.OutputSerializer(wish_list_for_user, many=True)
        return response.Response(output_serializer.data)


class WishListRetrieveUpdateDeleteAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        product = ProductSerializer()

    def delete(self, request, id, *args, **kwargs):
        wish_list = WishList(id=id)
        wish_list.delete()
        return response.Response("Removed Successfully", status=status.HTTP_200_OK)

    # def put(self, request, id, *args, **kwargs):

    def get(self, request, id, *args, **kwargs):
        wish_list = WishList.objects.filter(id=id).first()
        serializer = self.OutputSerializer(wish_list)
        return response.Response(serializer.data)
