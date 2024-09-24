from rest_framework import serializers
from products.products_model import ProductModel

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'  