from django.utils.text import slugify
from django import forms

from .models import Submission, Group
from .pictures import identify_picture_type

import hashlib

class ContentSubmissionForm(forms.Form):
    """A form for uploading submissions.
    The type of the submission is determined from the file itself.
    """
    submission = forms.FileField()

    def clean_submission(self):
        upload = self.cleaned_data['submission']
        
        picture_type = identify_picture_type(upload)
        
        if picture_type is None:
            raise forms.ValidationError("Unsupported file type")
        
        upload.content_type, suffix = picture_type
        
        h = hashlib.sha1()
        for chunk in upload.chunks():
            h.update(chunk)
        
        upload.name = h.hexdigest() + '.' + suffix

        return upload


class EditSubmissionForm(forms.ModelForm):
    """A form for editing the general submission attributes.
    """
    class Meta:
        model = Submission
        fields = ('title', 'description', 'is_nsfw', 'is_commenting_enabled', 'groups')
        widgets = {
            'groups': forms.CheckboxSelectMultiple
        }

    action = forms.CharField(required=False, widget=forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].choices = self.instance.uploaded_by.groupmembership_set.values_list('group_id', 'group__title').order_by('group__title')

    def save(self, commit=True):
        obj = super().save(False)

        cd = self.cleaned_data
        if cd['action'] == 'publish':
            obj.is_visible = True
        elif cd['action'] == 'hide':
            obj.is_visible = False

        if commit:
            obj.save()
            self.save_m2m()
        return obj


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'logo', 'description', 'server_address', 'website', 'approve_joins')
    
    def clean_title(self):
        title = self.cleaned_data['title']
        
        slug = slugify(title)

        if not slug:
            raise forms.ValidationError("Invalid title")

        if Group.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A group with a similar title already exists")

        return title
