from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'color', 'size', 'description', 'price']
        #fields = ['name', 'brand', 'color', 'size', 'description', 'price']
