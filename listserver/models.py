from django.db import models
from django.utils import timezone

from datetime import timedelta

class ListedSession(models.Model):
    TIMEOUT = 10 * 60  # Listing timeout in seconds

    host = models.CharField(max_length=255)
    port = models.IntegerField()
    session_id = models.CharField(max_length=255)
    protocol = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    users = models.IntegerField()
    password = models.BooleanField()
    nsfm = models.BooleanField()
    title = models.CharField(max_length=128)
    started = models.DateTimeField()
    last_active = models.DateTimeField()
    unlisted = models.BooleanField()
    client_ip = models.CharField(max_length=64)
    roomcode = models.CharField(max_length=16)
    private = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sessions'
        ordering = ('-last_active',)

    @property
    def is_live(self):
        return not self.unlisted and \
            self.last_active > timezone.now() - timedelta(seconds=self.TIMEOUT)


class Hostban(models.Model):
    host = models.CharField(max_length=255, primary_key=True)
    expires = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True)

    class Meta:
        managed = False
        db_table = 'hostbans'
        ordering = ('host',)

    def __str__(self):
        return self.host

