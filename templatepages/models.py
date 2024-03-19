from django.db import models
from django.utils import timezone
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField


class Image(models.Model):
    """An uploaded image that can be used in templates.
    Use the {% image %} tag to fetch the image.
    """

    name = models.SlugField(unique=True)
    alt_text = models.CharField(max_length=255)
    image = ThumbnailerImageField(upload_to="images")


class TemplateVar(models.Model):
    """A variable that can be set in the admin site.
    Use the {% templatevar %} tag to read this.
    """

    name = models.CharField(unique=True, max_length=32)
    text = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name
