from django.shortcuts import render

# Create your views here.
from rest_framework import views, response, status, permissions, serializers
from ecommerce.models.product import Product


class HomePageAPI(views.APIView):
    permission_classes = (permissions.AllowAny,)

    class ProductsOutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        description = serializers.CharField()
        image_url = serializers.CharField()
        price = serializers.FloatField()
        quantity = serializers.IntegerField()
        category = serializers.CharField()

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = self.ProductsOutputSerializer(queryset, many=True)
        return response.Response(serializer.data)
