from base64 import b64encode

from .settings import extauth_settings

import ed25519
import time
import calendar
import json

def make_login_token(username, flags, nonce, key=None):
    payload = {
        'username': username,
        'flags': flags,
        'nonce': nonce,
        'iat': calendar.timegm(time.gmtime()),
    }

    if isinstance(key, ed25519.SigningKey):
        signingkey = key
    else:
        signingkey = ed25519.SigningKey(key or extauth_settings['PRIVATE_KEY'])

    token = b'1.' + b64encode(json.dumps(payload).encode('utf-8'))
    signature = signingkey.sign(token, encoding='base64')

    token = token + b'.' + signature

    return token.decode('utf-8')

