from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

class PostManager(models.Manager):
    def visible(self):
        return self.get_queryset().filter(is_visible=True, publish__lte=timezone.now())

class Post(models.Model):
    slug = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[-.\w]+$')]
        )
    publish = models.DateTimeField()
    is_visible = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)

    intro = models.TextField()
    readmore = models.TextField(blank=True)

    objects = PostManager()

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

