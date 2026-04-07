from django.contrib.auth.hashers import check_password
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api.models import APIToken


class BearerTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if not auth_header.startswith("Bearer "):
            return None
        raw_token = auth_header[len("Bearer "):]
        for token in APIToken.objects.all():
            if check_password(raw_token, token.key_hash):
                return (None, token)
        raise AuthenticationFailed("Invalid token.")
