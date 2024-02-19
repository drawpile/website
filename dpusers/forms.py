from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django import forms
import re
from .token import parse_signup_token, parse_emailchange_token
from .models import EmailAddress, PendingDeletion
from .normalization import normalize_email
from dpauth.models import Username, username_pattern
import logging

logger = logging.getLogger(__name__)


_username_regex = re.compile(username_pattern)

def _username_valid(name):
    return bool(_username_regex.search(name))

def _email_already_registered(email, exclude_user_id=None):
    if get_user_model().objects.filter(email=email).exists():
        return True

    q = EmailAddress.objects.filter(
        normalized_address=normalize_email(email)
    )
    if exclude_user_id is not None:
        q = q.exclude(user_id=exclude_user_id)
    return q.exists()


class LoginForm(forms.Form):
    username = forms.CharField(label='Username or email address')
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=22)
    email = forms.EmailField()
    accept_tos = forms.BooleanField(required=True)
    program = forms.CharField(required=False)

    def clean_username(self):
        name = self.cleaned_data['username']
        if not _username_valid(name):
            raise forms.ValidationError("Invalid username.")

        if Username.exists(name):
            raise forms.ValidationError("This name is already taken.")

        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email, is_active=False).exists():
            raise forms.ValidationError("This user account has been blocked.")

        if _email_already_registered(email):
            raise forms.ValidationError('This email address has already been registered.')

        return email

    def clean_program(self):
        program = self.cleaned_data['program'].strip().casefold()
        expected = "drawpile"
        if program != expected:
            logger.warning("Spam protection hit with '%s'", program)
            raise forms.ValidationError("That's not what this program is called.")
        return expected


class FinishSignupForm(forms.Form):
    password = forms.CharField(
            widget=forms.PasswordInput,
            validators=[validate_password]
            )
    token = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        token = parse_signup_token(cleaned_data.get('token', ''))

        name = token['name']
        if not _username_valid(name):
            raise forms.ValidationError("Invalid username.")

        if Username.exists(token['name']):
            raise forms.ValidationError("This name is already taken.")

        if _email_already_registered(token['email']):
            raise forms.ValidationError('This email address has already been registered.')

        return cleaned_data


class EmailChangeForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if _email_already_registered(email, self.__user.id):
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
        user_id = self.__user.id

        if token['user'] != user_id:
            raise forms.ValidationError('This address change confirmation was meant for another user')

        if _email_already_registered(token['email'], user_id):
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

