from django.conf import settings

DEFAULTS = {
    'GUEST_LOGINS': True, # Support guest logins
    'ALT_COUNT': 4,       # Maximum number of usernames per account
    'PRIVATE_KEY': '',    # The login token signing key
    'PUBLIC_KEY': '',     # The login token verification key
}


extauth_settings = DEFAULTS.copy()
extauth_settings.update(getattr(settings, 'DRAWPILE_EXT_AUTH', {}))

