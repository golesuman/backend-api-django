from rest_framework import serializers

from ecommerce.models.product import Category, Product


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    image_url = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    category = CategorySerializer()
