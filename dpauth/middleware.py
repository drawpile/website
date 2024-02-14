from django.conf import settings


class AuthCorpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # The authentication is used as an iframe in an environment with CORP
        # headers set, so we need additional CORP and CSP headers for those.
        if request.path.startswith("/auth/"):
            response.headers["Cross-Origin-Resource-Policy"] = "same-site"
            response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
            response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
            response.headers[
                "Content-Security-Policy"
            ] = f"frame-ancestors {settings.DRAWPILE_AUTH_FRAME_ANCESTORS};"
        return response
