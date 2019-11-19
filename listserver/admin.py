from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe
from django import forms

# TODO we can use this in Django 2.2
#from django.contrib.humanize.templatetags.humanize import NaturalTimeFormatter

from datetime import timedelta

from .models import ListedSession, Hostban

DB = 'listserver'

class ActiveListFilter(admin.SimpleListFilter):
    title = "Status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return (
            ('active', 'Active'),
            ('recent', 'Recent'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.filter(
                unlisted=False,
                last_active__gte=timezone.now() - timedelta(seconds=ListedSession.TIMEOUT)
            )
        elif self.value() == 'recent':
            return queryset.filter(
                last_active__gte=timezone.now() - timedelta(seconds=ListedSession.TIMEOUT*2)
            )

        else:
            return queryset


def make_unlisted(modeladmin, request, queryset):
   queryset.using(DB).update(unlisted=True)
make_unlisted.short_description = "Unlist selected"

@admin.register(ListedSession)
class ListedSessionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'host', 'port', 'session_id', 'users', 'nsfw',
        'client_ip', 'uptime',
        )
    search_fields = ('title', 'host', 'session_id', 'client_ip')
    list_filter = (ActiveListFilter, 'nsfm', 'password', 'private')
    actions = (make_unlisted,)

    def uptime(self, obj):
        if obj.unlisted:
            return mark_safe('<b style="color: red">Unlisted (%s)</b>' % obj.started.date())
        if not obj.is_live:
            return mark_safe('<b style="color: orange">Expired (%s)</b>' % obj.started.date())

        delta = timezone.now() - obj.started
        val = ''
        if delta.days > 0:
            val = '%d days ' % delta.days

        if delta.seconds < (60*60):
            val += '%d minutes' % (delta.seconds // 60)
        else:
            val += '%.1f hours' % (delta.seconds / (60*60))

        return val
        # Django 2.2:
        #return NaturalTimeFormatter.string_for(obj.started)

    def nsfw(self, obj):
        if obj.nsfm:
            return 'NSFW'
        return ''

    def get_queryset(self, request):
        return super().get_queryset(request).using(DB)

    def delete_model(self, request, obj):
        obj.delete(using=DB)

    def has_add_permission(self, request):
        return False

    # TODO in Django 2.2, we'll have the view permission


# Hackery to make this work with a model that has a changeable primary key
class HostbanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        host = None
        try:
            if 'instance' in kwargs:
                host = kwargs['instance'].host
        except AttributeError:
            pass

        self._orig_host = host

    class Meta:
        model = Hostban
        fields = ('host', 'expires', 'notes')

    def validate_unique(self):
        newhost = self.cleaned_data['host']
        if self._orig_host != newhost and Hostban.objects.filter(host=newhost).using(DB).exists():
            self._update_errors(forms.ValidationError("This ban already exists"))


@admin.register(Hostban)
class HostbanAdmin(admin.ModelAdmin):
    list_display = ('host', 'expires', 'notes')
    #list_editable = ('host', 'expires', 'notes')
    #list_display_links = None

    def get_queryset(self, request):
        return super().get_queryset(request).using(DB)

    def get_form(self, request, obj=None, **kwargs):
        return HostbanForm

    def save_model(self, request, obj, form, change):
        if form._orig_host:
            Hostban.objects.filter(host=form._orig_host).using(DB).delete()
        obj.save(using=DB)

    def delete_model(self, request, obj):
        obj.delete(using=DB)

