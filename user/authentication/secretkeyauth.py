from rest_framework.authentication import get_authorization_header
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import BasePermission

class SecretKeyAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = get_authorization_header(request).decode('utf-8')
        if not auth_header or auth_header.split()[0].lower() != self.keyword.lower():
            return (None, None)

        try:
            token = auth_header.split()[1]
            return self.authenticate_credentials(token)
        except AuthenticationFailed:
            return (None, None)
    def authenticate_credentials(self, token):
        if token == settings.API_KEY:
            return ('', None)

        raise AuthenticationFailed('Invalid secret key')


class SecretKeyPermission(BasePermission):
    def has_permission(self, request, view):
        user, auth = SecretKeyAuthentication().authenticate(request)
        return user is not None