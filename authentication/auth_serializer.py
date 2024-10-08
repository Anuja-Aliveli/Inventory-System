from rest_framework import serializers

from authentication.auth_model import UserAuthentication

class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthentication
        fields = '__all__'  