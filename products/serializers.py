from rest_framework import serializers

from products.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'description', 'price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description')
