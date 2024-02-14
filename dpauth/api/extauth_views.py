from django.contrib.auth.hashers import check_password
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny

from dpauth.settings import extauth_settings
from dpauth.models import Username
from dpauth.api.auth_serializers import (
    AuthAttemptSerializer,
    CookieAuthAttemptSerializer,
    AccountQuerySerializer,
)

from importlib import import_module


class ExtAuthView(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if "password" in request.data:
            return Response(
                self.__handle_cookie_auth_attempt(request)
                if request.data["password"] is False
                else self.__handle_auth_attempt(request)
            )
        else:
            return Response(self.__handle_account_query(request))

    def __handle_auth_attempt(self, request):
        """A real authentication attempt."""
        serializer = AuthAttemptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = Username.getByName(data["username"])
        if username and not username.user.is_active:
            return {"status": "banned"}

        if not username or not check_password(data["password"], username.user.password):
            return {"status": "badpass"}

        return self.__finish_auth_attempt(data, username)

    def __handle_cookie_auth_attempt(self, request):
        """A real authentication attempt using a browser cookie."""
        serializer = CookieAuthAttemptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if not request.user.is_authenticated:
            return {"status": "badpass"}

        username = Username.getByName(data["username"])
        if username and not username.user.is_active:
            return {"status": "banned"}

        username = Username.getByName(data["username"])
        if not username or username.user_id != request.user.id:
            return {"status": "badpass"}

        return self.__finish_auth_attempt(data, username)

    def __finish_auth_attempt(self, data, username):
        group_membership = _group_membership_function()(username, data.get("group"))

        if group_membership is None:
            return {"status": "outgroup"}

        username.user.last_login = timezone.now()
        username.user.save(update_fields=("last_login",))

        return {
            "status": "auth",
            "token": username.make_login_token(
                data["nonce"],
                flags=group_membership["flags"],
                group=data.get("group"),
                avatar=data["avatar"],
            ),
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

        user = Username.getByName(data["username"])

        if user and not user.user.is_active:
            return {"status": "banned"}

        if extauth_settings["GUEST_LOGINS"]:
            return {
                "status": "auth" if user else "guest",
            }

        else:
            # If guest logins are not enabled, always just
            # return "auth"
            return {
                "status": "auth",
            }


class GroupMembershipImportError(Exception):
    pass


def _group_membership_function():
    impl = extauth_settings["GROUP_IMPL"]

    if isinstance(impl, str):
        modname, funcname = impl.rsplit(".", 1)
        try:
            mod = import_module(modname)
        except ImportError:
            raise GroupMembershipImportError(modname, "no such module")

        func = getattr(mod, funcname, None)
        if not hasattr(func, "__call__"):
            raise GroupMembershipImportError(impl, "does not point to a function!")

        # Cache the resolved function
        extauth_settings["GROUP_IMPL"] = func
        return func

    elif not hasattr(impl, "__call__"):
        raise GroupMembershipImportError(repr(impl), "not an import path or a function")

    return impl
