from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.utils.timezone import now

from . import models

import logging
logger = logging.getLogger(__name__)


@admin.register(models.Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_mod')
    readonly_fields = ('normalized_name',)
    search_fields = ('user__email', 'name')


class BanIpRangeForm(forms.ModelForm):
    class Meta:
        model = models.BanIpRange
        fields = ('from_ip', 'to_ip', 'excluded')
        widgets = {
            'excluded': forms.Select(choices=(
                (False, 'Ban this range'),
                (True, 'Exclude this range from the ban'),
            ))
        }

class BanIpRangeInline(admin.StackedInline):
    model = models.BanIpRange
    form = BanIpRangeForm
    extra = 1

class BanSystemIdentifierInline(admin.TabularInline):
    model = models.BanSystemIdentifier
    extra = 1

class BanUserForm(forms.ModelForm):
    class Meta:
        model = models.BanUser
        fields = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_widget = self.fields['user'].widget
        user_widget.can_add_related = False
        user_widget.can_change_related = False
        user_widget.can_delete_related = False

class BanUserInline(admin.TabularInline):
    model = models.BanUser
    form = BanUserForm
    extra = 1

@admin.register(models.Ban)
class IpBanAdmin(admin.ModelAdmin):
    fields = ('comment', 'expires', 'reason', 'reaction', 'reaction_includes_ipbans')
    list_display = ('id', 'comment', 'reason', 'expires', 'ban_type')
    list_display_links = list_display
    inlines = [BanIpRangeInline, BanSystemIdentifierInline, BanUserInline]
