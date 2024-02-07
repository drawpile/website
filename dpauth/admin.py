from django import forms
from django.conf import settings
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.utils.timezone import now

from . import models
from .webhooks import send_save_model_notification, send_delete_model_notification, send_delete_queryset_notification

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
    autocomplete_fields = ('user',)
    model = models.BanUser
    form = BanUserForm
    extra = 1

@admin.register(models.Ban)
class BanAdmin(admin.ModelAdmin):
    fields = ('comment', 'expires', 'reason', 'append_standard_reason', 'reaction', 'reaction_includes_ipbans')
    list_display = ('id', 'comment', 'full_reason', 'expires', 'ban_type')
    list_display_links = list_display
    inlines = [BanIpRangeInline, BanSystemIdentifierInline, BanUserInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_save_model_notification(webhook_url, request, change, ":hammer:", "Ban", obj.id)

    def delete_model(self, request, obj):
        obj_id = obj.id
        super().delete_model(request, obj)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_delete_model_notification(webhook_url, request, ":hammer:", "Ban", obj_id)

    def delete_queryset(self, request, queryset):
        obj_ids = list(queryset.all().values_list('id', flat=True))
        super().delete_queryset(request, queryset)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_delete_queryset_notification(webhook_url, request, ":hammer:", "Ban", obj_ids)

class UserVerificationForm(forms.ModelForm):
    class Meta:
        model = models.UserVerification
        fields = ('user', 'comment', 'exempt_from_bans')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_field = self.fields['user']
        user_widget = user_field.widget
        user_widget.can_add_related = False
        user_widget.can_change_related = False
        user_widget.can_delete_related = False
        instance = kwargs.get("instance")
        if instance and instance.user and instance.user.id:
            user_field.disabled = True

@admin.register(models.UserVerification)
class UserVerificationAdmin(admin.ModelAdmin):
    fields = ('user', 'comment', 'exempt_from_bans')
    autocomplete_fields = ('user',)
    list_display = ('user', 'comment', 'exempt_from_bans')
    list_display_links = list_display
    form = UserVerificationForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_save_model_notification(webhook_url, request, change, ":ballot_box_with_check:", "User Verification", obj.user_id)

    def delete_model(self, request, obj):
        obj_id = obj.user_id
        super().delete_model(request, obj)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_delete_model_notification(webhook_url, request, ":ballot_box_with_check:", "User Verification", obj_id)

    def delete_queryset(self, request, queryset):
        obj_ids = list(queryset.all().values_list('user_id', flat=True))
        super().delete_queryset(request, queryset)
        if webhook_url := getattr(settings, 'ADMIN_REPORT_WEBHOOK', ''):
            send_delete_queryset_notification(webhook_url, request, ":ballot_box_with_check:", "User Verification", obj_ids)
