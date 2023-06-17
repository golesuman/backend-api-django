from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, response, serializers, status, views

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
        query_params = self.request.GET.get("q")
        # if not query_params:
        if str(query_params).lower() == "null" or query_params is None:
            queryset = Product.objects.all().order_by("-name")

        else:
            queryset = Product.objects.filter(
                Q(category__name=query_params)
                | Q(name__contains=query_params)
                | Q(description__contains=query_params)
            ).order_by("-name")
        serializer = self.ProductsOutputSerializer(queryset, many=True)
        return response.Response(serializer.data)
