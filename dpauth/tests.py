from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from base64 import b64decode

from .normalization import normalize_username
from .token import make_login_token
from .models import Username

import ed25519
import json

class DpAuthTestCase(TestCase):
    def test_username_normalization(self):
        SAMPLES = (
            # (matching samples), (mismatching samples)
            (('abc', 'ABC', 'аbc'), ('äbc', 'ÄBC')),
            (('1xX', '1XX', '1⨯X'), ('2xx',)),
            )

        for sampleset in SAMPLES:
            first = normalize_username(sampleset[0][0])

            for match in sampleset[0]:
                self.assertEqual(first, normalize_username(match))

            for mismatch in sampleset[1]:
                self.assertNotEqual(first, normalize_username(mismatch))


class LoginTokenTest(TestCase):
    def test_token_generation(self):
        privkey, pubkey = ed25519.create_keypair()

        token = make_login_token(
            'bob',
            ['mod', 'host'],
            'deadbeef',
            key=privkey
            )

        version, payload, sig = token.split('.')

        self.assertEqual(version, '1')

        pubkey.verify(
            sig,
            (version + '.' + payload).encode('utf-8'),
            encoding='base64'
            )
        with self.assertRaises(ed25519.BadSignatureError):
            pubkey.verify(
                sig,
                (version + '...' + payload).encode('utf-8'),
                encoding='base64'
                )

        payload = json.loads(b64decode(payload.encode('utf-8')))
        self.assertEqual(payload['username'], 'bob')
        self.assertEqual(payload['flags'], ['mod', 'host'])
        self.assertEqual(payload['nonce'], 'deadbeef')
        self.assertEqual(type(payload['iat']), int)


class UserTest(TestCase):
    def setUp(self):
        U = get_user_model()
        u1 = U.objects.create(username='test1', email='test@example.com', password='abcd1324')
        u1.user_permissions.add(*Permission.objects.filter(codename='moderator'))
        u2 = U.objects.create(username='test2', email='test2@example.com', password='abcd1324')

        Username.objects.create(user=u1, name='test')
        Username.objects.create(user=u1, name='admin', is_mod=True)
        Username.objects.create(user=u2, name='another')
        Username.objects.create(user=u2, name='fakemod', is_mod=True)

    def test_token_creation(self):
        privkey, pubkey = ed25519.create_keypair()

        u1 = Username.getByName('test')
        token1 = json.loads(b64decode(u1.make_login_token('1234', key=privkey).split('.')[1]))

        self.assertEqual(token1['username'], 'test')
        self.assertFalse('mod' in token1['flags'])

        u2 = Username.getByName('admin')
        token2 = json.loads(b64decode(u2.make_login_token('1234', key=privkey).split('.')[1]))

        self.assertEqual(token2['username'], 'admin')
        self.assertTrue('mod' in token2['flags'])

        u3 = Username.getByName('fakemod')
        token3 = json.loads(b64decode(u3.make_login_token('1234', key=privkey).split('.')[1]))

        self.assertEqual(token3['username'], 'fakemod')
        self.assertFalse('mod' in token3['flags'])

