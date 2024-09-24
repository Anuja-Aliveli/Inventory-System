from django.db import models
from common import constants as ct
from authentication.auth_model import UserAuthentication

class ProductModel(models.Model):
    product_id = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, primary_key=True)
    product_name = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT)
    product_description = models.CharField(max_length=ct.CHAR_VERY_LONG_LIMIT)
    product_price = models.IntegerField(null=True, blank=True)  
    product_quantity = models.IntegerField(null=True, blank=True) 
    product_units = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserAuthentication, on_delete=models.CASCADE, related_name='user_products')
    
    class Meta:
        db_table = ct.PRODUCTS
