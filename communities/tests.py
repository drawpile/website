from rest_framework.test import APITestCase
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Community, Membership
from .extauth import community_membership_extauth
from dpauth.models import Username


class CommunityJoinTests(APITestCase):
    def setUp(self):
        U = get_user_model()
        self.u1 = U.objects.create_user(username='test1', password='test')

    def test_invite_only_join(self):
        c = make_test_community(policy=Community.GROUP_INVITE_ONLY)
        url = reverse('api:community-join', kwargs={'slug': 'test'})

        self.client.force_authenticate(self.u1)

        # Can't join without an invitation
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(0, Membership.objects.count())

        # Can join when invitation exists
        Membership.objects.create(
            community=c,
            user=self.u1,
            status=Membership.STATUS_INVITED)

        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Membership.STATUS_MEMBER,
            Membership.objects.all()[0].status)

        # Join request is idempotent
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, Membership.objects.count())
        self.assertEqual(
            Membership.STATUS_MEMBER,
            Membership.objects.all()[0].status)

    def test_free_join(self):
        make_test_community(policy=Community.GROUP_FREE_JOIN)

        url = reverse('api:community-join', kwargs={'slug': 'test'})
        self.client.force_authenticate(self.u1)

        # Can join directly
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            Membership.STATUS_MEMBER,
            Membership.objects.all()[0].status)

        # Join request is idempotent
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, Membership.objects.count())

    def test_verified_join(self):
        make_test_community(policy=Community.GROUP_VERIFIED_JOIN)

        url = reverse('api:community-join', kwargs={'slug': 'test'})
        self.client.force_authenticate(self.u1)

        # Can petition to join
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            Membership.STATUS_PENDING,
            Membership.objects.all()[0].status)

        # Join request is idempotent
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, Membership.objects.count())
        self.assertEqual(
            Membership.STATUS_PENDING,
            Membership.objects.all()[0].status)


class CommunityMemberlistTests(APITestCase):
    def setUp(self):
        U = get_user_model()

        self.community = make_test_community()
        self.memberlist_url = reverse(
            'api:community-members',
            kwargs={'slug': 'test'}
        )

        self.users = {'none': None}
        for status, label in Membership.STATUS_CHOICES:
            self.users[status] = U.objects.create(
                username=status,
                email='test@example.com',
                password='test'
            )

            Membership.objects.create(
                community=self.community,
                user=self.users[status],
                status=status
            )

    def test_hidden_memberlist(self):
        self.community.memberlist_visibility = Community.MEMBERLIST_HIDDEN
        self.community.save()

        for username, user in self.users.items():
            self.client.force_authenticate(user)

            response = self.client.get(self.memberlist_url)
            self.assertEqual(
                200 if username in Membership.MOD_STATUSES else 404,
                response.status_code,
                msg=username
            )

    def test_private_memberlist(self):
        self.community.memberlist_visibility = Community.MEMBERLIST_PRIVATE
        self.community.save()

        for username, user in self.users.items():
            self.client.force_authenticate(user)

            response = self.client.get(self.memberlist_url)
            self.assertEqual(
                200 if username in Membership.MEMBER_STATUSES else 404,
                response.status_code,
                msg=username
            )

    def test_public_memberlist(self):
        self.community.memberlist_visibility = Community.MEMBERLIST_VISIBLE
        self.community.save()

        for username, user in self.users.items():
            self.client.force_authenticate(user)

            response = self.client.get(self.memberlist_url)
            self.assertEqual(
                200,
                response.status_code,
                msg=username
            )
    
    def test_user_editing(self):
        """Only admin users should be able to edit memberships"""

        url = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.users['member']})

        for username, user in self.users.items():
            self.client.force_authenticate(user)
            response = self.client.put(url, {'status': 'member'})
            if username == 'none':
                expect = 403
            elif username == 'admin':
                expect = 200
            else:
                expect = 404

            self.assertEqual(
                expect,
                response.status_code,
                msg=username
            )


class CommunityDeletionTests(APITestCase):
    def setUp(self):
        self.community = make_test_community()
        U = get_user_model()
        self.u1 = U.objects.create_user(username='test1', password='test')
        self.u2 = U.objects.create_user(username='test2', password='test')
        self.u3 = U.objects.create_user(username='test3', password='test')
        self.u4 = U.objects.create_user(username='test4', password='test')

    def test_member_deletion(self):
        Membership.objects.create(
            community=self.community,
            user=self.u1,
            status=Membership.STATUS_MEMBER)
        Membership.objects.create(
            community=self.community,
            user=self.u2,
            status=Membership.STATUS_MEMBER)

        url1 = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u1.username})
        url2 = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u2.username})

        # Unauthenticated user can't delete anything
        self.client.force_authenticate(None)
        response = self.client.delete(url1)
        self.assertEqual(403, response.status_code)
        self.assertEqual(2, Membership.objects.count())

        # A normal member can't delete other members
        self.client.force_authenticate(self.u1)
        response = self.client.delete(url2)
        self.assertEqual(404, response.status_code)
        self.assertEqual(2, Membership.objects.count())

        # A normal member can delete themselves
        response = self.client.delete(url1)
        self.assertEqual(204, response.status_code)
        self.assertEqual(1, Membership.objects.count())

    def test_member_deletion_by_admin(self):
        Membership.objects.create(
            community=self.community,
            user=self.u1,
            status=Membership.STATUS_MEMBER)
        Membership.objects.create(
            community=self.community,
            user=self.u2,
            status=Membership.STATUS_ADMIN)

        url = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u1.username})

        self.client.force_authenticate(self.u2)
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)
        self.assertEqual(1, Membership.objects.count())

    def test_admin_deletion(self):
        Membership.objects.create(
            community=self.community,
            user=self.u1,
            status=Membership.STATUS_ADMIN)
        Membership.objects.create(
            community=self.community,
            user=self.u2,
            status=Membership.STATUS_MOD)
        Membership.objects.create(
            community=self.community,
            user=self.u3,
            status=Membership.STATUS_MEMBER)
        Membership.objects.create(
            community=self.community,
            user=self.u4,
            status=Membership.STATUS_INVITED)

        url1 = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u1.username})
        url2 = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u2.username})
        url3 = reverse(
            'api:community-member',
            kwargs={'slug': self.community.slug, 'user': self.u3.username})

        # Deleting the last admin will pass admin privilege to the fist mod
        self.client.force_authenticate(self.u1)
        response = self.client.delete(url1)
        self.assertEqual(204, response.status_code)
        self.assertEqual(3, Membership.objects.count())

        self.assertEqual(
            Membership.STATUS_ADMIN,
            Membership.objects.get(user=self.u2).status
        )

        # If there are no mods, privilege is passed to the oldest member
        self.client.force_authenticate(self.u2)
        response = self.client.delete(url2)
        self.assertEqual(204, response.status_code)
        self.assertEqual(2, Membership.objects.count())

        self.assertEqual(
            Membership.STATUS_ADMIN,
            Membership.objects.get(user=self.u3).status
        )

        # If there are no members, community is marked as rejected
        self.client.force_authenticate(self.u3)
        response = self.client.delete(url3)
        self.assertEqual(204, response.status_code)
        self.assertEqual(1, Membership.objects.count())
        self.assertEqual(
            Community.STATUS_REJECTED,
            Community.objects.all()[0].status)


class ExtAuthTests(TestCase):
    def setUp(self):
        U = get_user_model()
        self.community = make_test_community()
        self.u1 = U.objects.create_user(username='test1')
        self.u2 = U.objects.create_user(username='test2')
        self.u3 = U.objects.create_user(username='test3')
        self.un1 = Username.objects.create(
            user=self.u1,
            name=self.u1.username
        )
        self.un2 = Username.objects.create(
            user=self.u2,
            name=self.u2.username
        )
        self.un3 = Username.objects.create(
            user=self.u3,
            name=self.u3.username
        )
        self.membership = Membership.objects.create(
            user=self.u1,
            community=self.community,
            status=Membership.STATUS_MEMBER
        )
        self.membership3 = Membership.objects.create(
            user=self.u3,
            community=self.community,
            status=Membership.STATUS_PENDING
        )

    def test_hosting_privilege(self):
        # Everyone can host
        self.assertEqual(['HOST'], self._test(self.un1))
        self.assertEqual(['HOST'], self._test(self.un2))
        self.assertEqual(['HOST'], self._test(self.un3))
        
        # Only group members can host
        self.community.host_policy = Community.HOST_MEMBERS
        self.community.save()
        
        self.assertEqual(['HOST'], self._test(self.un1))
        self.assertEqual([], self._test(self.un2))
        self.assertEqual([], self._test(self.un3))
        
        # Only select members can host
        self.community.host_policy = Community.HOST_LIMITED
        self.community.save()
        
        self.assertEqual([], self._test(self.un1))
        self.assertEqual([], self._test(self.un2))
        self.assertEqual([], self._test(self.un3))
        
        self.membership.is_host = True
        self.membership.save()
        self.assertEqual(['HOST'], self._test(self.un1))

    def test_trusted_flag(self):
        U = get_user_model()

        # No automatically trusted members
        self.assertEqual(['HOST'], self._test(self.un1))
        self.assertEqual(['HOST'], self._test(self.un2))
        self.assertEqual(['HOST'], self._test(self.un3))

        # Explicitly flagged users
        self.membership3.status=Membership.STATUS_MEMBER
        self.membership3.is_trusted = True
        self.membership3.save()

        self.assertEqual(['HOST'], self._test(self.un1))
        self.assertEqual(['HOST'], self._test(self.un2))
        self.assertEqual(['HOST', 'TRUSTED'], self._test(self.un3))

        # Group members trusted
        self.community.trust_members = True
        self.community.save()
        
        self.assertEqual(['HOST', 'TRUSTED'], self._test(self.un1))
        self.assertEqual(['HOST'], self._test(self.un2))
        self.assertEqual(['HOST', 'TRUSTED'], self._test(self.un3))

    def test_banned_login(self):
        self.membership.status = Membership.STATUS_BANNED
        self.membership.save()
        
        self.assertEqual(None, self._test(self.un1))
        self.assertEqual(['HOST'], self._test(self.un2))
        self.assertEqual(['HOST'], self._test(self.un3))

    def test_closed_group(self):
        self.community.require_group_membership = True
        self.community.save()

        self.assertEqual(['HOST'], self._test(self.un1))
        self.assertEqual(None, self._test(self.un2))
        self.assertEqual(None, self._test(self.un3))

    def _test(self, user):
        x = community_membership_extauth(user, self.community.slug)
        if x is None:
            return None
        else:
            return x['flags']


def make_test_community(
        slug="test",
        policy=Community.GROUP_INVITE_ONLY,
        memberlist=Community.MEMBERLIST_HIDDEN,
        status=Community.STATUS_ACCEPTED
        ):
    return Community.objects.create(
        title="Test",
        slug=slug,
        short_description="",
        full_description="",
        badge="",
        rules="",
        group_policy=policy,
        memberlist_visibility=memberlist,
        drawpile_server="",
        list_server="",
        homepage="",
        guests_allowed=False,
        trust_members=False,
        host_policy=Community.HOST_EVERYONE,
        account_host="drawpile.net",
        require_group_membership=False,
        status=status
    )
