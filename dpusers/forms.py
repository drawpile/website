from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django import forms
from .token import parse_signup_token, parse_emailchange_token
from .models import EmailAddress, PendingDeletion, SentEmail
from .normalization import normalize_email
from dpauth.models import Username, username_pattern
import django.contrib.auth.forms as auth_forms
import logging
import re

logger = logging.getLogger(__name__)


_username_regex = re.compile(username_pattern)


def _username_valid(name):
    return bool(_username_regex.search(name))


def _email_already_registered(email, exclude_user_id=None):
    if get_user_model().objects.filter(email=email).exists():
        return True

    q = EmailAddress.objects.filter(normalized_address=normalize_email(email))
    if exclude_user_id is not None:
        q = q.exclude(user_id=exclude_user_id)
    return q.exists()


class LoginForm(forms.Form):
    username = forms.CharField(label="Username or email address")
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=22)
    email = forms.EmailField()
    accept_tos = forms.BooleanField(required=True)
    program = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            SentEmail.validate_total_limit(SentEmail.EmailType.SIGNUP, email)
        return cleaned_data

    def clean_username(self):
        name = self.cleaned_data["username"]
        if not _username_valid(name):
            raise forms.ValidationError("Invalid username.")

        if Username.exists(name):
            raise forms.ValidationError("This name is already taken.")

        return name

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email, is_active=False).exists():
            raise forms.ValidationError("This user account has been blocked.")

        if _email_already_registered(email):
            raise forms.ValidationError(
                "This email address has already been registered."
            )

        SentEmail.validate_address_limit(SentEmail.EmailType.SIGNUP, email)
        return email

    def clean_program(self):
        program = self.cleaned_data["program"].strip().casefold()
        expected = "drawpile"
        if program != expected:
            logger.warning("Signup spam protection hit with '%s'", program)
            raise forms.ValidationError("That's not what this program is called.")
        return expected


class FinishSignupForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password]
    )
    token = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        token = parse_signup_token(cleaned_data.get("token", ""))

        name = token["name"]
        if not _username_valid(name):
            raise forms.ValidationError("Invalid username.")

        if Username.exists(token["name"]):
            raise forms.ValidationError("This name is already taken.")

        if _email_already_registered(token["email"]):
            raise forms.ValidationError(
                "This email address has already been registered."
            )

        return cleaned_data


class EmailChangeForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            SentEmail.validate_total_limit(SentEmail.EmailType.EMAIL_CHANGE, email)
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]

        if _email_already_registered(email, self.__user.id):
            raise forms.ValidationError(
                "This email address has already been registered."
            )

        SentEmail.validate_address_limit(SentEmail.EmailType.EMAIL_CHANGE, email)
        return email


class ConfirmEmailChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    token = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data["password"]

        if not self.__user.check_password(password):
            raise forms.ValidationError("Incorrect password!")

        return password

    def clean(self):
        cleaned_data = super().clean()
        token = parse_emailchange_token(cleaned_data.get("token", ""))
        user_id = self.__user.id

        if token["user"] != user_id:
            raise forms.ValidationError(
                "This address change confirmation was meant for another user"
            )

        if _email_already_registered(token["email"], user_id):
            raise forms.ValidationError(
                "This email address has already been registered."
            )

        return cleaned_data


class ConfirmDeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.__user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data["password"]

        if not self.__user.check_password(password):
            raise forms.ValidationError("Incorrect password!")

        return password


class ResetPasswordForm(auth_forms.PasswordResetForm):
    program = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            SentEmail.validate_total_limit(SentEmail.EmailType.PASSWORD_RESET, email)
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        SentEmail.validate_address_limit(SentEmail.EmailType.PASSWORD_RESET, email)
        return email

    def clean_program(self):
        program = self.cleaned_data["program"].strip().casefold()
        expected = "drawpile"
        if program != expected:
            logger.warning("Reset password spam protection hit with '%s'", program)
            raise forms.ValidationError("That's not what this program is called.")
        return expected

    def get_users(self, email):
        users = list(super().get_users(email))
        count = len(users)
        if count == 1:
            return users
        elif count > 1:
            logger.warning(
                "Multiple users registered to email %s, using first one", email
            )
            return [users[0]]
        elif count == 0:
            logger.info(
                "Not sending password recovery to unregistered email '%s'", email
            )
            return []

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        user = context["user"]
        logger.info(
            "Sending password recovery for '%s' (%d) to '%s'",
            user.username,
            user.id,
            to_email,
        )
        SentEmail.store_sent_email(SentEmail.EmailType.PASSWORD_RESET, to_email)
        super().send_mail(
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name,
        )
