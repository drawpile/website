from django import forms
from django.core.exceptions import ValidationError

from .models import Community
from .utils import downscale_image_if_necessary
from . import serverchecks

import logging
logger = logging.getLogger(__name__)

class EditCommunityForm(forms.ModelForm):
    ACCOUNTS_NONE = 'none'
    ACCOUNTS_HERE = 'here'
    ACCOUNTS_HERE_GROUP = 'here/group'
    ACCOUNTS_OTHER = 'other'

    ACCOUNT_POLICY = (
        (ACCOUNTS_NONE, 'Guest users only'),
        (ACCOUNTS_HERE, 'Uses drawpile.net accounts'),
        (ACCOUNTS_HERE_GROUP,
            'Uses drawpile.net accounts and requires group membership'),
        (ACCOUNTS_OTHER, 'Accounts from:')
    )

    account_policy = forms.ChoiceField(
        choices=ACCOUNT_POLICY,
        widget=forms.RadioSelect(),
    )
    other_accounts = forms.CharField(max_length=200, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        self._do_serverchecks = instance is None
        if instance is not None:
            self.fields['slug'].disabled = True

            if not instance.account_host:
                self.fields['account_policy'].initial = self.ACCOUNTS_NONE
            elif instance.account_host == 'drawpile.net':
                self.fields['account_policy'].initial = (
                    self.ACCOUNTS_HERE_GROUP
                    if instance.require_group_membership
                    else self.ACCOUNTS_HERE
                )
            else:
                self.fields['account_policy'].initial = self.ACCOUNTS_OTHER
                self.fields['other_accounts'].initial = instance.account_host

    class Meta:
        model = Community
        fields = (
            'title', 'slug', 'short_description', 'full_description', 'badge',
            'region', 'rules', 'group_policy', 'memberlist_visibility',
            'drawpile_server', 'list_server', 'homepage',
            'guests_allowed', 'host_policy', 'trust_members',
            'content_rating', 'web_policy',
        )
        widgets = {
            'group_policy': forms.RadioSelect(),
            'memberlist_visibility': forms.RadioSelect(),
            'host_policy': forms.RadioSelect(),
            'content_rating': forms.RadioSelect(),
            'web_policy': forms.RadioSelect(),
        }
    
    def clean_badge(self):
        badge = self.cleaned_data['badge']
        return downscale_image_if_necessary(badge, (400, 200))

    def clean_homepage(self):
        url = self.cleaned_data['homepage']

        if url and self._do_serverchecks:
            logger.info("%s: Checking website: %s",
                self.cleaned_data.get('slug'),
                url
            )
            try:
                serverchecks.check_website(url)
            except serverchecks.ServerCheckFailed as e:
                logger.info("%s: Checking website: %s: Error: %s",
                    self.cleaned_data.get('slug'),
                    url,
                    e.message
                )
                raise ValidationError(e.message)

        return url

    def clean_list_server(self):
        url = self.cleaned_data['list_server']

        if url and self._do_serverchecks:
            logger.info("%s: Checking list server: %s",
                self.cleaned_data.get('slug'),
                url
            )
            try:
                serverchecks.check_listserver(url)
            except serverchecks.ServerCheckFailed as e:
                logger.info("%s: Checking list server: %s: Error: %s",
                    self.cleaned_data.get('slug'),
                    url,
                    e.message
                )
                raise ValidationError(e.message)

        return url

    def clean_drawpile_server(self):
        url = self.cleaned_data['drawpile_server']

        if url:
            try:
                other = Community.objects\
                    .filter(drawpile_server=url, status=Community.STATUS_ACCEPTED)\
                    .exclude(slug=self.cleaned_data['slug'])[0]
            except IndexError:
                pass
            else:
                raise ValidationError('This server belongs to "%s".' % other.title)

        if url and self._do_serverchecks:
            logger.info("%s: Checking drawpile server: %s",
                self.cleaned_data.get('slug'),
                url
            )
            try:
                serverchecks.check_drawpile_server(url)
            except serverchecks.ServerCheckFailed as e:
                logger.info("%s: Checking drawpile server: %s: Error: %s",
                    self.cleaned_data.get('slug'),
                    url,
                    e.message
                )
                raise ValidationError(e.message)

        return url

    def clean(self):
        cd = super().clean()

        if not cd.get('drawpile_server') and not cd.get('list_server'):
            self.add_error(
                'drawpile_server',
                'Specify at least one of these'
            )
            self.add_error(
                'list_server',
                'Specify at least one of these'
            )

        if (
            cd['account_policy'] == self.ACCOUNTS_OTHER and
            not cd['other_accounts']
        ):
            self.add_error(
                'other_accounts',
                'Server name must be set when external accounts are in use.'
            )

    def save(self):
        cd = self.cleaned_data

        obj = super().save(commit=False)

        if cd['account_policy'] == self.ACCOUNTS_NONE:
            obj.account_host = ''
            obj.require_group_membership = False
        elif cd['account_policy'] == self.ACCOUNTS_HERE:
            obj.account_host = 'drawpile.net'
            obj.require_group_membership = False
        elif cd['account_policy'] == self.ACCOUNTS_HERE_GROUP:
            obj.account_host = 'drawpile.net'
            obj.require_group_membership = True
        elif cd['account_policy'] == self.ACCOUNTS_OTHER:
            obj.account_host = cd['other_accounts']
            obj.require_group_membership = False

        if obj.status == Community.STATUS_RESUBMIT:
            obj.status = Community.STATUS_SUBMITTED

        obj.save()
        return obj


class ReviewForm(forms.Form):
    VERDICTS = (
        (Community.STATUS_ACCEPTED, "Accept and publish"),
        (Community.STATUS_RESUBMIT, "Needs changes"),
        (Community.STATUS_REJECTED, "Reject as unsuitable"),
    )

    verdict = forms.ChoiceField(
        choices=VERDICTS,
        widget=forms.RadioSelect()
        )

    comment = forms.CharField(
        widget=forms.Textarea(),
        required=False
        )
