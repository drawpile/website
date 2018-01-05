from django.utils.crypto import salted_hmac
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

import calendar
import time
import json

def make_signup_token(username, email):
    """Generate a token that allows a new account to be created for
    the given username and email combination.
    """

    return _make_token({
        'name': username,
        'email': email,
    }, 'dp.net.user.signup')

def parse_signup_token(token):
    return _parse_token(token, 'dp.net.user.signup')


def make_emailchange_token(user_id, email):
    """Generate an email change confirmation token.
    """
    return _make_token({
        'user': user_id,
        'email': email,
    }, 'dp.net.user.emailchange')

def parse_emailchange_token(token):
    return _parse_token(token, 'dp.net.user.emailchange')


def _make_token(payload, salt):
    payload['ts'] = calendar.timegm(time.gmtime())

    token = urlsafe_base64_encode(json.dumps(payload).encode('utf-8'))
    mac = salted_hmac(salt, token)

    return (token + b'.' + urlsafe_base64_encode(mac.digest())).decode('utf-8')

def _parse_token(token, salt):
    try:
        payload, sig = token.split('.')
    except ValueError:
        raise ValidationError("Invalid signup link!")

    mac = salted_hmac(salt, payload).digest()

    if mac != urlsafe_base64_decode(sig):
        raise ValidationError("Corrupted signup link!")

    content = json.loads(urlsafe_base64_decode(payload))

    if content['ts'] < calendar.timegm(time.gmtime()) - (60 * 60 * 1):
        raise ValidationError("Link has expired!")

    return content

