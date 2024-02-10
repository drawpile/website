from django.conf import settings
from django.db import models


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
