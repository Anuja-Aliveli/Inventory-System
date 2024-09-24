import jwt
from django.http import  JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from common import constants as ct
from django.conf import settings
from django.contrib.auth.hashers import check_password

from authentication.auth_model import UserAuthentication

@api_view(['POST'])
def user_login(request):
    user_name = request.data.get(ct.USER_NAME)
    password = request.data.get(ct.PASSWORD)
    try:
        user = UserAuthentication.objects.filter(user_name=user_name).get()
        if user:
            is_correct_password = check_password(password, user.password)
            if is_correct_password:
                # Generate JWT token
                payload = {ct.USER_ID: user.user_id}
                jwt_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
                return JsonResponse({ct.MESSAGE: ct.USER_LOGIN_SUCCESSFUL, ct.TOKEN: jwt_token, ct.USER_NAME: user.user_name}, status=status.HTTP_200_OK)
            else:
                raise Exception(ct.LOGIN_INVALID_DATA_ERROR)
        else:
            raise Exception(ct.USER_NOT_FOUND)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)