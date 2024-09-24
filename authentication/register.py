from django.http import JsonResponse
from rest_framework.decorators import api_view
from common import constants as ct
from rest_framework import status
from django.contrib.auth.hashers import make_password
from inventory_system.authentication.auth_model import UserAuthentication
from inventory_system.authentication.auth_serializer import UserAuthenticationSerializer
from inventory_system.common.utils import generate_id, get_latest_id

# Password Validations
def validate_password(password):
    check_password = False
    if len(password) < 6:
        raise Exception(ct.PASSWORD_LENGTH_ERROR)
    else:
        number_count = 0
        small_letter_count = 0
        caps_count = 0
        symbol_count = 0
        for letter in password:
            if letter.isupper():
                caps_count += 1
            elif letter.islower():
                small_letter_count += 1 
            elif letter.isdigit():
                number_count += 1
            else:
                symbol_count += 1
        if number_count == 0 and small_letter_count == 0 and caps_count == 0 and symbol_count == 0:
            raise Exception(ct.PASSWORD_TYPES_ERROR)
        elif caps_count == 0:
            raise Exception(ct.PASSWORD_CAPITAL_ERROR)
        elif symbol_count == 0:
            raise Exception(ct.PASSWORD_SYMBOL_ERROR)
        elif number_count == 0:
            raise Exception(ct.PASSWORD_NUMBER_ERROR)
        else:
            check_password = True
    return check_password

@api_view(['POST'])
def user_registration(request):
    password = request.data.get(ct.PASSWORD, None)
    user_name = request.data.get(ct.USER_NAME, None)
    try:
        is_valid_password = validate_password(password)
        if is_valid_password:
            latest_user = get_latest_id(UserAuthentication, ct.USER_ID)
            user_data = {
                ct.USER_NAME: user_name,
                ct.USER_ID: generate_id(ct.USR,latest_user),
                ct.PASSWORD: make_password(password),
            }
            serializer = UserAuthenticationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({ct.MESSAGE: ct.USER_REGISTER_SUCCESSFUL}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)
    