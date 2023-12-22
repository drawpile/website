from django.db import models
from django.conf import settings
from django.urls import reverse

from .utils import UploadNameFromContent

community_badge_upload_to = UploadNameFromContent('community/badges/', 'badge')


class Community(models.Model):
    STATUS_SUBMITTED = 'submitted'
    STATUS_RESUBMIT = 'resubmit'
    STATUS_ACCEPTED = 'accepted'
    STATUS_REJECTED = 'rejected'
    STATUSES = (
        (STATUS_SUBMITTED, 'Submitted, awaiting review'),
        (STATUS_RESUBMIT, 'Reviewed, awaiting resubmission'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_REJECTED, 'Rejected (with prejudice)'),
    )

    GROUP_INVITE_ONLY = 'invite-only'
    GROUP_FREE_JOIN = 'free-join'
    GROUP_VERIFIED_JOIN = 'verified-join'
    GROUP_POLICY = (
        (GROUP_INVITE_ONLY, 'Invitation only'),
        (GROUP_FREE_JOIN, 'Anyone can join'),
        (GROUP_VERIFIED_JOIN,
            'Anyone can join, but must be verified by a moderator'),
    )

    HOST_EVERYONE = 'all-host'
    HOST_MEMBERS = 'member-host'
    HOST_LIMITED = 'limited-host'
    HOST_POLICY = (
        (HOST_EVERYONE, 'Everyone can host sessions'),
        (HOST_MEMBERS, 'Only group members can host'),
        (HOST_LIMITED, 'Only select users can host'),
    )

    MEMBERLIST_HIDDEN = 'hidden'
    MEMBERLIST_PRIVATE = 'private'
    MEMBERLIST_VISIBLE = 'visible'
    MEMBERLIST_VISIBILITY = (
        (MEMBERLIST_HIDDEN, 'Hidden'),
        (MEMBERLIST_PRIVATE, 'Visible to other members only'),
        (MEMBERLIST_VISIBLE, 'Visible to all logged in users'),
    )

    CONTENT_SFW = 'sfw'
    CONTENT_MIXED = 'mixed'
    CONTENT_ADULT = 'adult'
    CONTENT_RATINGS = (
        (CONTENT_SFW, "Safe-For-Work content only"),
        (CONTENT_MIXED, "Adult content is permitted but must be tagged"),
        (CONTENT_ADULT, "This is an adults only community"),
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    title = models.CharField(
        max_length=100,
        help_text="The name of your community")
    slug = models.SlugField(
        unique=True,
        help_text="Short name (consisting only of letters a-z, numbers, "
                  "underscores or hyphens) for use in links. Note: this cannot " 
                  "be changed afterwards, except by site admins.")
    short_description = models.TextField()
    full_description = models.TextField()
    badge = models.ImageField(
        upload_to=community_badge_upload_to,
        # validators=[community_logo_validator]
        )

    rules = models.TextField()
    group_policy = models.CharField(
        verbose_name="Group membership",
        max_length=32,
        choices=GROUP_POLICY,
        default=GROUP_INVITE_ONLY)
    memberlist_visibility = models.CharField(
        verbose_name="Member list",
        max_length=32,
        choices=MEMBERLIST_VISIBILITY,
        default=MEMBERLIST_HIDDEN)

    drawpile_server = models.CharField(
        max_length=100,
        blank=True,
        help_text="The hostname of your drawpile server, if any. "
                  "(Include the port too, if not the default.)"
        )
    list_server = models.URLField(
        blank=True,
        help_text="The URL to your list server, if any."
        )
    homepage = models.URLField(
        blank=True,
        help_text="The URL to your homepage, if any."
        )

    guests_allowed = models.BooleanField(
        verbose_name="Guest users can log in",
        default=True)

    account_host = models.CharField(max_length=200, blank=True)

    require_group_membership = models.BooleanField(default=False)

    trust_members = models.BooleanField(
        default=False,
        verbose_name="Group members get the 'Trusted' flag"
    )

    host_policy = models.CharField(
        verbose_name="Who can host sessions?",
        max_length=16,
        choices=HOST_POLICY,
        default=HOST_EVERYONE
    )

    content_rating = models.CharField(max_length=16, choices=CONTENT_RATINGS, default=CONTENT_MIXED)

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='communities.Membership'
    )

    status = models.CharField(
        max_length=32,
        choices=STATUSES,
        default=STATUS_SUBMITTED
    )
    review_message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "communities"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('communities:community', kwargs={'slug': self.slug})

    @property
    def moderators(self):
        return Membership.objects.filter(
            community=self,
            status__in=Membership.MOD_STATUSES
        ).order_by('joined').select_related('user')
    
    def is_member(self, user):
        return self.membership_set.active().filter(user=user).exists()

    def can_login(self, user):
        dp_accounts = self.account_host == 'drawpile.net'

        if self.guests_allowed or not dp_accounts:
            return True
        
        if not user.is_authenticated:
            return False
        
        return not self.require_group_membership or self.is_member(user)

    def can_admin(self, user):
        return user.is_authenticated and (
            user.has_perm('communities.change_community') or
            Membership.objects.filter(
                community=self, user=user,
                status=Membership.STATUS_ADMIN
            ).exists()
        )

    def can_see_memberlist(self, user):
        vis = self.memberlist_visibility
        return (
            vis == self.MEMBERLIST_VISIBLE or (
                user.is_authenticated and (
                    user.has_perm('communities.change_community') or
                    Membership.objects.filter(
                        community=self, user=user,
                        status__in=(
                            Membership.MEMBER_STATUSES
                            if vis == self.MEMBERLIST_PRIVATE
                            else Membership.MOD_STATUSES
                        )
                    ).exists()
                )
            )
        )


class MembershipQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status__in=Membership.MEMBER_STATUSES)


class Membership(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_INVITED = 'invited'
    STATUS_MEMBER = 'member'
    STATUS_MOD = 'mod'
    STATUS_ADMIN = 'admin'
    STATUS_BANNED = 'banned'
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending approval'),
        (STATUS_INVITED, 'Invited'),
        (STATUS_MEMBER, 'Member'),
        (STATUS_MOD, 'Moderator'),
        (STATUS_ADMIN, 'Admin'),
        (STATUS_BANNED, 'Banned'),
        )
    MOD_STATUSES = (STATUS_MOD, STATUS_ADMIN)
    MEMBER_STATUSES = (STATUS_MEMBER,) + MOD_STATUSES

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE
    )
    joined = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    is_host = models.BooleanField(default=False)
    is_trusted = models.BooleanField(default=False)
    is_ghost = models.BooleanField(default=False)

    ban_reason = models.CharField(
        max_length=200,
        blank=True,
        help_text="Why this user was banned. "
                  "Visible to admins and this user only."
    )

    objects = MembershipQuerySet.as_manager()

    class Meta:
        unique_together = ('user', 'community')

    @property
    def is_mod(self):
        return self.status in self.MOD_STATUSES

    @property
    def is_admin(self):
        return self.status == self.STATUS_ADMIN

    @property
    def is_member(self):
        return self.status in self.MEMBER_STATUSES

    def get_mod_username(self):
        """Return the first Username associated with this
        user that has the Mod flag set, or the primary username
        if there is none.
        """
        return self.user.drawpilename_set\
            .filter(models.Q(name=self.user.username)|models.Q(is_mod=True))\
            .order_by('-is_mod')[0]
