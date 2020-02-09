from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django import forms

from .token import parse_signup_token, parse_emailchange_token
from dpauth.models import Username

class LoginForm(forms.Form):
    username = forms.CharField(label='Username or email address')
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=22)
    email = forms.EmailField()
    accept_tos = forms.BooleanField(required=True)

    def clean_username(self):
        name = self.cleaned_data['username']
        if Username.exists(name):
            raise forms.ValidationError("This name is already taken.")

        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email, is_active=False).exists():
            raise forms.ValidationError("This user account has been blocked.")
        return email


class FinishSignupForm(forms.Form):
    password = forms.CharField(
            widget=forms.PasswordInput,
            validators=[validate_password]
            )
    token = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        token = parse_signup_token(cleaned_data.get('token', ''))

        if Username.exists(token['name']):
            raise forms.ValidationError("Oh no! Someone just reserved this name!")

        if get_user_model().objects.filter(email=token['email']).exists():
            raise forms.ValidationError('This email address has already been registered.')

        return cleaned_data


class EmailChangeForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email address has already been registered.')

        return email


class ConfirmEmailChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    token = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.__user.check_password(password):
            raise forms.ValidationError('Incorrect password!')

        return password

    def clean(self):
        cleaned_data = super().clean()
        token = parse_emailchange_token(cleaned_data.get('token', ''))

        if token['user'] != self.__user.id:
            raise forms.ValidationError('This address change confirmation was meant for another user')

        if get_user_model().objects.filter(email=token['email']).exists():
            raise forms.ValidationError('This email address has already been registered.')

        return cleaned_data


class ConfirmDeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.__user.check_password(password):
            raise forms.ValidationError('Incorrect password!')

        return password

