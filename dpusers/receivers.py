from django.contrib.auth import get_user_model
from django.db.models.functions import Now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmailAddress
from .normalization import normalize_email


@receiver(post_save, sender=get_user_model())
def create_or_update_email_address_after_user_saved(
    sender, instance, created, raw, *args, **kwargs
):
    if not raw:
        raw_address = instance.email
        normalized_address = normalize_email(raw_address)
        try:
            email_address = EmailAddress.objects.get(pk=instance.id)
        except EmailAddress.DoesNotExist:
            email_address = EmailAddress(user_id=instance.id)

        has_change = (
            raw_address != email_address.raw_address
            or normalized_address != email_address.normalized_address
        )
        if has_change:
            email_address.raw_address = raw_address
            email_address.normalized_address = normalized_address
            email_address.save()
