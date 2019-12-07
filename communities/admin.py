from django.contrib import admin

from . import models


class MembershipAdmin(admin.TabularInline):
    model = models.Membership
    extra = 0


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    inlines = (MembershipAdmin,)
