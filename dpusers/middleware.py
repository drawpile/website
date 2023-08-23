import time
from django.utils.http import http_date

class UsernameCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            empty = request.session.is_empty()
        except AttributeError:
            return response

        username = request.user.username
        has_cookie = 'username' in request.COOKIES
        if username:
            if not has_cookie:
                if request.session.get_expire_at_browser_close():
                    max_age = None
                    expires = None
                else:
                    max_age = request.session.get_expiry_age()
                    expires_time = time.time() + max_age
                    expires = http_date(expires_time)
                response.set_cookie(
                    'username',
                    username,
                    max_age=max_age,
                    expires=expires,
                    domain='drawpile.net',
                    httponly=False,
                    samesite='Lax',
                )
        elif has_cookie:
            response.delete_cookie('username', domain='drawpile.net')

        return response
