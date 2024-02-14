from django import forms
from .models import Username


class AuthUsernamesForm(forms.Form):
    username = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_username(self):
        name = self.cleaned_data["username"]
        if self.__user.drawpilename_set.filter(name=name).exists():
            return name
        else:
            raise forms.ValidationError(f'Username "{name}" does not exist.')
