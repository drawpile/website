from django.contrib import admin

from news.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'publish', 'is_visible')

