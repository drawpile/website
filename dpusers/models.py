from django.conf import settings
from django.forms import ValidationError
from django.db import models
from django.utils import timezone
from datetime import timedelta
from .normalization import normalize_email
import logging

logger = logging.getLogger(__name__)


class EmailAddress(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    raw_address = models.CharField(
        max_length=255,
        help_text="Verbatim email address used to register the account",
    )
    normalized_address = models.CharField(
        max_length=255,
        help_text="Normalized email address for querying",
    )

    class Meta:
        indexes = [
            models.Index(fields=["normalized_address"]),
        ]


class PendingDeletion(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    deactivated_at = models.DateTimeField(
        help_text="When deletion was initiated by the user",
    )


class SentEmail(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=["normalized_address"]),
            models.Index(fields=["sent_at"]),
        ]

    class EmailType(models.IntegerChoices):
        SIGNUP = 1
        PASSWORD_RESET = 2
        EMAIL_CHANGE = 3

    email_type = models.IntegerField(
        choices=EmailType.choices,
        help_text="What kind of email this was",
    )
    raw_address = models.CharField(
        max_length=255,
        help_text="Verbatim email address",
    )
    normalized_address = models.CharField(
        max_length=255,
        help_text="Normalized email address for querying",
    )
    sent_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="When the email was sent",
    )

    @classmethod
    def validate_address_limit(cls, email_type, raw_address):
        cutoff = timezone.now() - timedelta(hours=1)
        address_per_hour = cls.objects.filter(
            sent_at__gte=cutoff, normalized_address=normalize_email(raw_address)
        ).count()
        max_address_per_hour = settings.DRAWPILE_EMAIL_MAX_ADDRESS_PER_HOUR
        if address_per_hour >= max_address_per_hour:
            logger.warning(
                "Address hourly email limit %d >= %d for type %d to '%s'",
                address_per_hour,
                max_address_per_hour,
                email_type,
                raw_address,
            )
            raise ValidationError(
                "Too many requests for this address. If the emails are not "
                + "arriving, check the help page on how to get in contact."
            )

    @classmethod
    def validate_total_limit(cls, email_type, raw_address):
        cls._validate_total_limit_per_hours(
            email_type, raw_address, 1, settings.DRAWPILE_EMAIL_MAX_TOTAL_PER_HOUR
        )
        cls._validate_total_limit_per_hours(
            email_type, raw_address, 24, settings.DRAWPILE_EMAIL_MAX_TOTAL_PER_DAY
        )

    @classmethod
    def _validate_total_limit_per_hours(cls, email_type, raw_address, hours, max_total):
        cutoff = timezone.now() - timedelta(hours=hours)
        total = cls.objects.filter(sent_at__gte=cutoff).count()
        if total >= max_total:
            logger.warning(
                "Total %d-hour email limit %d >= %d for type %d to '%s'",
                hours,
                total,
                max_total,
                email_type,
                raw_address,
            )
            cls._raise_total_limit_validation_error(email_type)

    @classmethod
    def _raise_total_limit_validation_error(cls, email_type):
        if email_type == cls.EmailType.SIGNUP:
            message = (
                "The website's email queue is full, so it can't send you a "
                + "signup link right now. Please take a look at the help "
                + "page on how to get in contact, an administrator can "
                + "send it manually."
            )
        elif email_type == cls.EmailType.PASSWORD_RESET:
            message = (
                "The website's email queue is full, so password reset "
                + "links can't be sent right now. Please take a look at "
                + "the help page on how to get in contact, an "
                + "administrator can send it manually."
            )
        elif email_type == cls.EmailType.EMAIL_CHANGE:
            message = (
                "The website's email queue is full, so a confirmation "
                + "link can't be sent right now. Either try again later "
                + "or check out the help pages on how to get in contact, "
                + "an administrator can send it manually."
            )
        else:
            message = (
                "The website's email queue is full, so this operation "
                + "can't be completed right now. Either try again later "
                + "or check out the help pages on how to get in contact."
            )
        raise ValidationError(message)

    @classmethod
    def store_sent_email(cls, email_type, raw_address):
        obj = cls(
            email_type=email_type,
            raw_address=raw_address,
            normalized_address=normalize_email(raw_address),
        )
        obj.save()
