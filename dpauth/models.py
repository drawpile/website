from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .normalization import normalize_username
from .token import make_login_token
from .utils import UploadNameFromContent, AvatarValidator

import datetime
import ipaddress
import logging
logger = logging.getLogger(__name__)


avatar_upload_to = UploadNameFromContent('avatar/', 'avatar')
avatar_validator = AvatarValidator(max_dims=(64, 64))
username_pattern = r'^[^"@]{1,22}$'


class Username(models.Model):
    """A Drawpile username.
    A single account may have multiple alternative usernames.

    A normalized version of the name is generated for internal use.
    The normalized version is used when querying a username to prevent
    deceptively similar names. (E.g. names differing by case or using
    homoglyphs to appear identical.)

    The "dpauth.moderator" permission makes a user a moderator. The moderator
    privilege can then be activated on a per-username basis.

    The "dpauth.ghost" permission also lets that user assign ghost status to
    usernames.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='drawpilename_set'
    )

    name = models.CharField(max_length=22,
        help_text="The original username",
        validators=[RegexValidator(
            username_pattern,
            message="Invalid username"
        )]
    )
    normalized_name = models.CharField(
        max_length=255,
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
    is_ghost = models.BooleanField(
        default=False,
        help_text="Enable ghost status for this username if the user has the ghost permission."
    )

    class Meta:
        indexes = [
            models.Index(fields=["normalized_name"]),
        ]
        permissions = (
            ("moderator", "Can activate moderator privileges"),
            ("ghost", "Can activate ghost privileges"),
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
            return Username.objects\
                .select_related('user')\
                .get(normalized_name=normalize_username(name))
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

    def make_login_token(self, nonce, flags=[], group=None, avatar=False, key=None):
        """Generate a login token for this user.

        Parameters:
        nonce  -- the random number that identifies this login attempt
        flags  -- list of user flags
        avatar -- if True, include the avatar (if present)
        key    -- the signing key to use (default is the one set in extauth_settings)

        Returns a login token string
        """

        avatar_image = None
        if avatar and self.avatar:
            try:
                avatar_image = self.avatar.read()
            except:
                logger.exception("Error reading avatar")

        return make_login_token(
            self.name,
            self.user_id,
            flags,
            nonce,
            group,
            avatar_image,
            key=key
        )


class Ban(models.Model):
    class Reactions(models.TextChoices):
        NORMAL = "normal", "Normal ban: disconnect and tell client they're banned"
        NETERROR = "neterror", "Shadow ban: disconnect with a bogus network error"
        GARBAGE = "garbage", "Shadow ban: send garbage responses in the login process"
        HANG = "hang", "Shadow ban: hang the login process forever with no response"
        TIMER = "timer", "Shadow ban: sever connection after a random time elapses"

    STANDARD_TEXT = "If you think this ban is an error, take a look at https://drawpile.net/ban/ on how to contact a moderator."

    expires = models.DateField(
        verbose_name="Until",
        default=datetime.date.fromisoformat("9999-12-31"),
        help_text="Date until which this ban lasts",
    )
    comment = models.TextField(
        help_text="Reason and other notes for the ban, only mods can read this",
    )
    reason = models.CharField(
        max_length=255,
        blank=True,
        help_text="Reason for the ban shown to the user, may be left empty",
    )
    append_standard_reason = models.BooleanField(
        verbose_name="Append standard text to reason",
        default=True,
        help_text=f"Will append the following: \"{STANDARD_TEXT}\"",
    )
    reaction = models.CharField(
        max_length=16,
        choices = Reactions.choices,
        default = Reactions.NORMAL,
        help_text="Shadow bans may help slow down ban evaders, not applied to IPs by default",
    )
    reaction_includes_ipbans = models.BooleanField(
        verbose_name="Apply shadow bans to IPs",
        default=False,
        help_text="NOT RECOMMENDED! False positives will confuse the heck out of legitimate users",
    )

    @property
    def ban_type(self):
        if self.reaction == Ban.Reactions.NORMAL:
            return "normal"
        elif self.reaction_includes_ipbans:
            return f"SHADOW+IP: {self.reaction}"
        else:
            return f"shadow: {self.reaction}"

    @property
    def full_reason(self):
        if self.reason:
            if self.append_standard_reason:
                return f"{self.reason} {Ban.STANDARD_TEXT}"
            else:
                return self.reason
        elif self.append_standard_reason:
            return Ban.STANDARD_TEXT
        else:
            return None

    def __str__(self):
        return f"Ban ({self.id}) {repr(self.comment)} reason {repr(self.reason)} expires {self.expires}"

    def clean(self):
        self.reason = self.reason.strip()
        if self.reason and self.append_standard_reason and len(f"{self.reason} {Ban.STANDARD_TEXT}") > 255:
            raise ValidationError({"reason": "Reason plus standard text must not exceed 255 characters"})


class BanIpRange(models.Model):
    class Meta:
        verbose_name = "IP Range"

    from_ip = models.CharField(
        verbose_name="Start of IP Range",
        max_length=64,
        help_text="IPv4 or IPv6 address",
    )
    to_ip = models.CharField(
        verbose_name="End of IP Range (inclusive)",
        max_length=64,
        blank=True,
        help_text="Leave empty to affect only a single address",
    )
    excluded = models.BooleanField(
        verbose_name="Exclusion",
        default=False,
    )
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE)

    def __str__(self):
        prefix = "Exclusion" if self.excluded else "Ban"
        address = f"{self.from_ip}-{self.to_ip}" if self.to_ip else self.from_ip
        return f"IP {prefix} {address} on ban {self.ban_id}"

    def clean(self):
        errors = {}

        try:
            from_ip = ipaddress.ip_address(self.from_ip)
        except ValueError:
            errors["from_ip"] = "Invalid IP address"

        if self.to_ip:
            try:
                to_ip = ipaddress.ip_address(self.to_ip)
            except ValueError:
                errors["to_ip"] = "Invalid IP address"
        else:
            to_ip = None

        if errors:
            raise ValidationError(errors)

        if to_ip:
            if from_ip.version != to_ip.version:
                errors["to_ip"] = "IP version doesn't match range start"
                raise ValidationError(errors)

            if from_ip.packed > to_ip.packed:
                errors["to_ip"] = "Range end is before its start"
                raise ValidationError(errors)


class BanSystemIdentifier(models.Model):
    class Meta:
        verbose_name = "System Identifier"

    identifier = models.CharField(
        max_length=64,
        help_text="UUID, shown in ClientInfo server logs under \"s\"",
        validators=[RegexValidator(
            r'^[0-9a-fA-F]{32}$',
            message="Must be 32 characters of 0123456789abcdef"
        )]
    )
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE)

    def __str__(self):
        return f"SID {repr(self.identifier)} on ban {self.ban_id}"


class BanUser(models.Model):
    class Meta:
        verbose_name = "User"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE)

    def __str__(self):
        return f"User ({self.user.id}) on ban {self.ban_id}"


class UserVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    comment = models.TextField(
        help_text="Verification reason, provide links to socials/galleries if possible",
    )
    exempt_from_bans = models.BooleanField(
        verbose_name="Exempt from IP bans",
        default=False,
        help_text="System ID, user and session bans still hold regardless",
    )

    def __str__(self):
        return f"Verification of user ({self.user.id})"
