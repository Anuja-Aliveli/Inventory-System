from django.db import models
from common import constants as ct

class UserAuthentication(models.Model):
    user_id = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, primary_key=True)
    user_name = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = ct.USER_AUTHENTICATION