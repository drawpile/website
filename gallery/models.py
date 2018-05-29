from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from gallery.utils import UploadNameFromContent, AvatarValidator
from gallery.validators import hostname_validator

group_logo_upload_to = UploadNameFromContent('gallery/groups/', 'logo')
group_logo_validator = AvatarValidator(max_dims=(128, 128))

class Group(models.Model):
    """The group model represents a user group within the gallery.
    """
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    logo = models.ImageField(
        blank=True,
        upload_to=group_logo_upload_to,
        validators=[group_logo_validator])
    
    description = models.TextField(
        max_length=10000,
        blank=True,
        help_text="A short introduction of this group"
    )

    server_address = models.CharField(
        max_length=128,
        blank=True,
        help_text="You group's home server",
        validators=[hostname_validator]
    )
    
    website = models.URLField(
        blank=True,
        help_text="Your group's web site"
    )

    approve_joins = models.BooleanField(
        default=False,
        help_text="Moderator must approve new users"
    )

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='gallery.GroupMembership'
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery:group-detail', kwargs={'slug': self.slug})
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                raise ValidationError("Invalid title")
        
        return super().save()

    def can_edit(self, user):
        return user.is_authenticated and (
            user.has_perm('gallery.change_group') or \
            self.groupmembership_set.filter(user=user, status=GroupMembership.STATUS_MOD).exists()\
        )


class GroupMembership(models.Model):
    """User's membership in a group
    """
    STATUS_PENDING = 'pending'
    STATUS_MEMBER = 'member'
    STATUS_MOD = 'mod'
    STATUS_BANNED = 'banned'
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending approval'),
        (STATUS_MEMBER, 'Member'),
        (STATUS_MOD, 'Moderator'),
        (STATUS_BANNED, 'Banned'),
    )
    MEMBER_STATUSES = (STATUS_MEMBER, STATUS_MOD)

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    joined = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('group', 'user')

    @property
    def is_mod(self):
        return self.status == self.STATUS_MOD
    
    @property
    def is_member(self):
        return self.status in self.MEMBER_STATUSES


avatar_upload_to = UploadNameFromContent('gallery/avatar/', 'avatar')
avatar_validator = AvatarValidator(max_dims=(64, 64))

class GalleryProfile(models.Model):
    """User's info used in the gallery.
    
    This includes public info, as well as private settings.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
        )
    
    # Public info
    avatar = models.ImageField(
        blank=True,
        upload_to=avatar_upload_to,
        validators=[avatar_validator])

    bio = models.TextField(
        max_length=10000,
        blank=True,
        help_text="Introduce yourself"
    )
    
    # User settings (private)
    show_nsfw = models.BooleanField(default=False)
    
    @staticmethod
    def get_prefs(user):
        """Get the viewing preferences for the given user.
        """
        
        prof = None
        fields = ('show_nsfw',)
        if user.is_authenticated:
            try:
                prof = GalleryProfile.objects.only(*fields).get(user=user)
            except GalleryProfile.DoesNotExist:
                pass
        
        if prof:
            return {f: getattr(prof, f) for f in fields}
        else:
            return {f: False for f in fields}


class Submission(models.Model):
    """An item that has been submitted to the gallery.
    """
    TYPE_PICTURE = 'picture'
    TYPES = (
        (TYPE_PICTURE, 'Picture'),
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    submission_type = models.CharField(max_length=16, choices=TYPES)
    thumbnail = models.ImageField(upload_to='gallery/thumbs/')

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)

    is_visible = models.BooleanField(default=False)
    is_nsfw = models.BooleanField(verbose_name='NSFW', default=False)
    is_commenting_enabled = models.BooleanField(verbose_name='Allow comments', default=True)

    groups = models.ManyToManyField(Group, blank=True)
    favorited_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='gallery.Favorited',
        related_name='favorite_submission_set'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery:view-submission', kwargs={'pk': self.id})
    
    @property
    def content(self):
        if self.submission_type == self.TYPE_PICTURE:
            return self.picture
        else:
            raise ValueError("Unhandled type: " + self.submission_type)

    def can_edit(self, user):
        return user.is_authenticated and (user.has_perm('gallery.change_submission') or self.uploaded_by == user)

    def can_comment(self, user):
        return user.is_authenticated and self.is_visible and self.is_commenting_enabled

    @staticmethod
    def get_total_size(user):
        """Get the total size of the given user's uploads."""
        return Picture.objects.filter(submission__uploaded_by=user).aggregate(models.Sum('filesize'))['filesize__sum'] or 0


class Picture(models.Model):
    """Picture type submission content
    """
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        primary_key=True
        )

    downscaled = models.ImageField(upload_to='gallery/downscaled/', blank=True)
    fullsize = models.FileField(upload_to='gallery/full/')
    filesize = models.PositiveIntegerField()

    def __str__(self):
        return 'Picture #%d' % self.submission_id

    def get_download_url(self):
        return self.fullsize.url

# TODO additional types: recordings, palettes, animations, etc.


class Favorited(models.Model):
    """Users' favorite submissions
    """
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('submission', 'user')


class Comment(models.Model):
    """A comment made to a submission
    """
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=2000)
    
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def can_delete(self, user):
        return user.is_authenticated and \
            (user.has_perm('gallery.delete_comment') or \
            user == self.user or \
            user == self.submission.uploaded_by)

    def can_undelete(self, user):
        return user.is_authenticated and \
            (user.has_perm('gallery.delete_comment') or \
            user == self.submission.uploaded_by)

