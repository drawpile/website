from django.contrib.auth.hashers import check_password
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny

from .settings import extauth_settings
from .models import Username
from .serializers import AuthAttemptSerializer, AccountQuerySerializer

class ExtAuthView(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if 'password' in request.data:
            return Response(self.__handle_auth_attempt(request))
        else:
            return Response(self.__handle_account_query(request))

    def __handle_auth_attempt(self, request):
        """A real authentication attempt.
        """
        serializer = AuthAttemptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = Username.getByName(data['username'])
        if username and not username.user.is_active:
            return {
                "status": "banned"
            }

        if not username or not check_password(data['password'], username.user.password):
            return {
                "status": "badpass"
            }
   
        username.user.last_login = timezone.now()
        username.user.save(update_fields=('last_login',))

        return {
            "status": "auth",
            "token": username.make_login_token(data['nonce'])
        }


    def __handle_account_query(self, request):
        """A user account existence query.
        This request is made by the server when guest logins are enabled.

        If guest logins are not enabled on this side, this will always
        return "auth" (except for banned users.)
        """
        serializer = AccountQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = Username.getByName(data['username'])

        if user and not user.user.is_active:
            return {
                "status": "banned"
            }

        if extauth_settings['GUEST_LOGINS']:
            return {
                "status": "auth" if user else "guest",
            }

        else:
            # If guest logins are not enabled, always just
            # return "auth"
            return {
                "status": "auth",
            }

