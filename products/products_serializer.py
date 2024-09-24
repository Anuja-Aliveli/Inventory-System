from rest_framework import serializers
from products.products_model import ProductManager

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManager
        fields = '__all__'  