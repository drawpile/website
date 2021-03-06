from rest_framework.test import APITestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse

from base64 import b64decode

from .normalization import normalize_username
from .token import make_login_token
from .models import Username
from .settings import extauth_settings, null_group_membership
from .api.extauth_views import GroupMembershipImportError, _group_membership_function

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
            1,
            ['MOD', 'HOST'],
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

        payload = json.loads(b64decode(payload.encode('utf-8')).decode('utf-8'))
        self.assertEqual(payload['username'], 'bob')
        self.assertEqual(payload['uid'], 1)
        self.assertEqual(payload['flags'], ['MOD', 'HOST'])
        self.assertEqual(payload['nonce'], 'deadbeef')
        self.assertEqual(type(payload['iat']), int)

    def test_token_generation_with_avatar(self):
        privkey, pubkey = ed25519.create_keypair()

        token = make_login_token(
            'bob',
            1,
            ['MOD'],
            'deadbeef',
            avatar_image=b'123456789',
            key=privkey
            )

        version, payload, avatar, sig = token.split('.')

        self.assertEqual(version, '2')

        pubkey.verify(
            sig,
            (version + '.' + payload + '.' + avatar).encode('utf-8'),
            encoding='base64'
            )
        with self.assertRaises(ed25519.BadSignatureError):
            pubkey.verify(
                sig,
                (version + '...' + payload).encode('utf-8'),
                encoding='base64'
                )

        payload = json.loads(b64decode(payload.encode('utf-8')).decode('utf-8'))
        self.assertEqual(payload['username'], 'bob')
        self.assertEqual(payload['uid'], 1)
        self.assertEqual(payload['flags'], ['MOD'])
        self.assertEqual(payload['nonce'], 'deadbeef')
        self.assertEqual(b64decode(avatar), b'123456789')
        self.assertEqual(type(payload['iat']), int)


def dummy_group_membership(username, group):
    if group:
        return None
    return {
        'member': False,
        'flags': []
    }


class AuthApiTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        priv, pub = ed25519.create_keypair()
        extauth_settings.update({
            'PRIVATE_KEY': priv.to_bytes(),
            'PUBLIC_KEY': pub.to_bytes(),
        })
        cls.url = reverse('api:ext-auth-view')

    @classmethod
    def tearDownClass(cls):
        extauth_settings['GROUP_IMPL'] = null_group_membership

    def setUp(self):
        U = get_user_model()
        self.u1 = U.objects.create_user(username='test1', password='abc')
        self.u2 = U.objects.create_user(username='test2', password='abc', is_active=False)
        self.u3 = U.objects.create_user(username='test3', password='abc')

        self.un1 = Username.objects.create(user=self.u1, name=self.u1.username)
        self.un2 = Username.objects.create(user=self.u2, name=self.u2.username)
        self.un3 = Username.objects.create(user=self.u3, name=self.u3.username)

        extauth_settings['GROUP_IMPL'] = null_group_membership

    def test_account_query(self):
        test_table = (
            # Guest, username, status
            (True, self.u1.username, 'auth'),
            (True, 'no-such-user', 'guest'),
            (True, self.u2, 'banned'),
            (False, self.u1.username, 'auth'),
            (False, 'no-such-user', 'auth'),
            (False, self.u2, 'banned'),
        )

        for guest, username, status in test_table:
            extauth_settings['GUEST_LOGINS'] = guest
            response = self.client.post(self.url, data={
                'username': username,
            })
            self.assertEqual(200, response.status_code)
            self.assertEqual(status, response.json()['status'])

    def test_authentication(self):
        test_table = (
            # username, password, status
            (self.u1.username, 'abc', 'auth'),
            (self.u1.username, 'xyz', 'badpass'),
            ('no-such-user', 'abc', 'badpass'),
            (self.u2.username, 'abc', 'banned'),
        )
        for username, password, status in test_table:
            response = self.client.post(self.url, data={
                'username': username,
                'password': password,
                'nonce': '0001',
            })
            self.assertEqual(200, response.status_code, msg=username)
            self.assertEqual(status, response.json()['status'], msg=username)

    def _membership_testfunc(self, username, group):
        self.assertTrue(group == "testg")

        # Allow guests
        if username is None and extauth_settings['GUEST_LOGINS']:
            return {
                'member': False,
                'flags': []
            }

        # Only specific registered users are accepted
        if username is None or username.name != self.u1.username:
            return None

        return {
            'member': True,
            'flags': ['HOST']
        }

    def test_group_function(self):
        test_table = (
            # username, group, status
            (self.u1.username, '', 'auth'),
            (self.u1.username, 'test', 'outgroup'),
        )

        with self.assertRaises(GroupMembershipImportError):
            extauth_settings['GROUP_IMPL'] = 'nosuchmodule.function'
            _group_membership_function()

        extauth_settings['GROUP_IMPL'] = 'dpauth.tests.dummy_group_membership'
        for username, group, status in test_table:
            response = self.client.post(self.url, data={
                'username': username,
                'password': 'abc',
                'group': group,
                'nonce': '0001',
            })
            self.assertEqual(200, response.status_code, msg=username)
            self.assertEqual(status, response.json()['status'], msg=username)

    def test_group_authentication(self):
        extauth_settings['GROUP_IMPL'] = self._membership_testfunc
        test_table = (
            # username, password, status
            (self.u1.username, 'abc', 'auth'),
            (self.u1.username, 'xyz', 'badpass'),
            ('no-such-user', 'abc', 'badpass'),
            (self.u2, 'abc', 'banned'),
            (self.u3, 'abc', 'outgroup'),
        )

        for username, password, status in test_table:
            response = self.client.post(self.url, data={
                'username': username,
                'password': password,
                'group': 'testg',
                'nonce': '0002',
            })
            self.assertEqual(200, response.status_code, msg=username)
            self.assertEqual(status, response.json()['status'], msg=username)


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
        token1 = json.loads(b64decode(u1.make_login_token('1234', key=privkey).split('.')[1]).decode('utf-8'))
        self.assertEqual(token1['username'], 'test')

        u2 = Username.getByName('admin')
        token2 = json.loads(b64decode(u2.make_login_token('1234', key=privkey).split('.')[1]).decode('utf-8'))
        self.assertEqual(token2['username'], 'admin')

        u3 = Username.getByName('fakemod')
        token3 = json.loads(b64decode(u3.make_login_token('1234', key=privkey).split('.')[1]).decode('utf-8'))
        self.assertEqual(token3['username'], 'fakemod')


class UsernameApiTest(APITestCase):
    def setUp(self):
        U = get_user_model()
        self.u1 = U.objects.create_user(username='test1', password='test')
        self.name1 = Username.objects.create(
            user=self.u1,
            name=self.u1.username
        )
        self.name2 = Username.objects.create(
            user=self.u1,
            name="alt1"
        )

        self.u2 = U.objects.create_user(username='test2', password='test')
        self.name3 = Username.objects.create(
            user=self.u2,
            name=self.u2.username
        )

    def test_auth(self):
        # Non-logged in users see nothing
        url = reverse('api:username-list')
        self.client.force_authenticate(None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        # Logged in users see their own usernames
        self.client.force_authenticate(self.u1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(response.json()))

    def test_name_limit(self):
        url = reverse('api:username-list')
        self.client.force_authenticate(self.u1)

        can_create = extauth_settings['ALT_COUNT'] - 2
        for i in range(can_create):
            response = self.client.post(url, data={'name': 'user%d' % i})
            self.assertEqual(response.status_code, 201)
        
        response = self.client.post(url, data={'name': 'toomany'})
        self.assertEqual(response.status_code, 400)

    def test_duplicate_name(self):
        url = reverse('api:username-list')
        self.client.force_authenticate(self.u1)
        
        response = self.client.post(url, data={'name': self.u1.username})
        self.assertEqual(response.status_code, 400)

    def test_make_primary(self):
        url = reverse('api:username-detail', kwargs={'name': self.name2.name})
        self.client.force_authenticate(self.u1)

        response = self.client.patch(url, data={'is_primary': True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.name2.name,
            get_user_model().objects.get(pk=self.u1.pk).username
        )
    
    def test_update(self):
        url = reverse('api:username-detail', kwargs={'name': self.name1.name})
        self.client.force_authenticate(self.u1)

        response = self.client.patch(url, data={'is_mod': True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            True,
            Username.objects.get(name=self.name1.name).is_mod
        )

    def test_deletion(self):
        url1 = reverse('api:username-detail', kwargs={'name': self.name1.name})
        url2 = reverse('api:username-detail', kwargs={'name': self.name2.name})
        self.client.force_authenticate(self.u1)

        # Deleting the primary name makes an alt the new primary
        response = self.client.delete(url1)
        self.assertEqual(204, response.status_code)
        self.u1 = get_user_model().objects.get(pk=self.u1.pk)
        self.assertEqual(
            self.name2.name,
            self.u1.username
        )
        self.assertEqual(1, Username.objects.filter(user=self.u1).count())

        # Can't delete the last name
        self.client.force_authenticate(self.u1)
        self.name2.user = self.u1
        response = self.client.delete(url2)
        self.assertEqual(400, response.status_code)
        self.assertEqual(1, Username.objects.filter(user=self.u1).count())
