import jwt
from django.conf import settings
from django.http import JsonResponse
from common import constants as ct

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.urls_without_token = ct.TOKEN_NOT_REQUIRED_FOR_URLS

    def __call__(self, request):
        # Extract JWT token from request headers
        path = request.path_info
        if path in self.urls_without_token:
            # No token authentication required for this URL
            return self.get_response(request)
        jwt_token = request.headers.get('Authorization', '')
        if jwt_token:
            token_parts = jwt_token.split(' ')
            if len(token_parts) == 2 and token_parts[0] == 'Bearer':
                jwt_token = token_parts[1]
                try:
                    # Verify JWT token
                    payload = jwt.decode(jwt_token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
                    print(payload)
                    user_id = payload.get(ct.USER_ID)
                    request.user_id = user_id
                    # Token is valid, allow the request to proceed
                    return self.get_response(request)
                except jwt.ExpiredSignatureError:
                    return JsonResponse({ct.ERROR: ct.JWT_TOKEN_EXPIRED}, status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({ct.ERROR: ct.JWT_INVALID_TOKEN}, status=401)
            else:
                # Invalid token format
                return JsonResponse({ct.ERROR: ct.JWT_INVALID_TOKEN}, status=401)
        else:
            # No Authorization header provided
            return JsonResponse({ct.ERROR: ct.JWT_TOKEN_REQUIRED}, status=401)