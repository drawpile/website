from base64 import b64encode

from .settings import extauth_settings

import ed25519
import time
import calendar
import json

def make_login_token(username, user_id, flags, nonce, group=None, avatar_image=None, key=None):
    version = b'1.'

    payload = {
        'username': username,
        'flags': flags,
        'nonce': nonce,
        'iat': calendar.timegm(time.gmtime()),
        'uid': user_id,
    }

    if avatar_image:
        avatar_image = b'.' + b64encode(avatar_image)
        version = b'2.'
    else:
        avatar_image = b''

    if group:
        payload['group'] = group

    if isinstance(key, ed25519.SigningKey):
        signingkey = key
    else:
        signingkey = ed25519.SigningKey(key or extauth_settings['PRIVATE_KEY'])

    token = version + b64encode(json.dumps(payload).encode('utf-8')) + avatar_image
    signature = signingkey.sign(token, encoding='base64')

    token = token + b'.' + signature

    return token.decode('utf-8')

