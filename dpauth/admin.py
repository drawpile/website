from django.contrib import admin

from . import models

@admin.register(models.Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_mod')
    readonly_fields = ('normalized_name',)
    search_fields = ('user__email', 'name')

