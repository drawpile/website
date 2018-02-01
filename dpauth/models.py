from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from .normalization import normalize_username
from .token import make_login_token

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
    def exists(name):
        """Check if the given name has been registered
        """
        return Username.objects.filter(normalized_name=normalize_username(name)).exists()

    def make_login_token(self, nonce, key=None):
        """Generate a login token for this user.

        Parameters:
        nonce -- the random number that identifies this login attempt
        key -- the signing key to use (default is the one set in extauth_settings)

        Returns a login token string
        """

        flags = ['HOST'] # all users have hosting privileges at the moment
        if self.is_mod and self.user.has_perm('dpauth.moderator'):
            flags.append('MOD')

        return make_login_token(self.name, self.user_id, flags, nonce, key=key)

