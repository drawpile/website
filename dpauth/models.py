from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ObjectDoesNotExist

from .normalization import normalize_username
from .token import make_login_token
from .utils import UploadNameFromContent, AvatarValidator

import logging
logger = logging.getLogger(__name__)


avatar_upload_to = UploadNameFromContent('avatar/', 'avatar')
avatar_validator = AvatarValidator(max_dims=(64, 64))


class Username(models.Model):
    """A Drawpile username.
    A single account may have multiple alternative usernames.

    A normalized version of the name is generated for internal use.
    The normalized version is used when querying a username to prevent
    deceptively similar names. (E.g. names differing by case or using
    homoglyphs to appear identical.)

    The "dpauth.moderator" permission makes a user a moderator. The moderator
    privilege can then be activated on a per-username basis.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='drawpilename_set'
    )

    name = models.CharField(max_length=22,
        help_text="The original username",
        validators=[RegexValidator(
            r'^[^"]{1,22}$',
            message="Invalid username"
        )]
    )
    normalized_name = models.CharField(
        max_length=22,
        unique=True,
        blank=True, # this field gets autoassigned in the clean() method
        help_text="Normalized username for querying"
    )
    is_mod = models.BooleanField(
        default=False,
        help_text="Enable moderator status for this username if the user has the moderator permission."
    )
    avatar = models.ImageField(
        blank=True,
        upload_to=avatar_upload_to,
        validators=[avatar_validator]
    )

    class Meta:
        permissions = (
            ("moderator", "Can activate moderator privileges"),
        )
        ordering = ['user', 'id']

    def __str__(self):
        return self.name

    def clean(self):
        # Make sure the name is updated before validate_unique is called
        self.normalized_name = normalize_username(self.name)

    def save(self, *args, **kwargs):
        self.normalized_name = normalize_username(self.name)
        super().save(*args, **kwargs)

    @property
    def is_primary(self):
        return self.user.username == self.name

    def make_primary(self):
        self.user.username = self.name
        self.user.save(update_fields=('username',))

    @staticmethod
    def getByName(name):
        """Normalize the username and find a username entry that matches it.

        Returns None if no such username is found.
        """
        try:
            return Username.objects.get(normalized_name=normalize_username(name))
        except Username.DoesNotExist:
            return None

    @staticmethod
    def exists(name, except_for=None):
        """Check if the given name has been registered
        """
        qs = Username.objects.filter(normalized_name=normalize_username(name))
        if except_for is not None:
            qs = qs.filter(~models.Q(pk=except_for))
        return qs.exists()

    def make_login_token(self, nonce, avatar=False, key=None):
        """Generate a login token for this user.

        Parameters:
        nonce  -- the random number that identifies this login attempt
        avatar -- if True, include the avatar (if present)
        key    -- the signing key to use (default is the one set in extauth_settings)

        Returns a login token string
        """

        flags = ['HOST'] # all users have hosting privileges at the moment
        if self.is_mod and self.user.has_perm('dpauth.moderator'):
            flags.append('MOD')

        avatar_image = None
        if avatar and self.avatar:
            try:
                avatar_image = self.avatar.read()
            except:
                logger.exception("Error reading avatar")

        return make_login_token(self.name, self.user_id, flags, nonce, avatar_image, key=key)

