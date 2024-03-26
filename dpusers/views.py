from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import TemplateView, FormView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.utils import timezone
from dpauth.models import Username
from dpauth.settings import extauth_settings
from communities.models import Membership
from django.contrib.auth import views as auth_views
from .models import PendingDeletion
from .forms import (
    SignupForm,
    FinishSignupForm,
    EmailChangeForm,
    ConfirmEmailChangeForm,
    ConfirmDeleteAccountForm,
    ResetPasswordForm,
)
from .token import (
    make_signup_token,
    parse_signup_token,
    make_emailchange_token,
    parse_emailchange_token,
)
from .mail import send_template_mail

import logging

logger = logging.getLogger(__name__)


class SignupView(FormView):
    """New user signup: first phase.

    This doesn't save anything in the database yet. Instead, it generates
    a token for the next phase, which actually creates the account.
    The token is mailed to the given email address to ensure the
    address is real.

    If the email address is registered already, a password recovery mail is
    sent instead.
    """

    template_name = "registration/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:finish-signup")

    def form_valid(self, form):
        cd = form.cleaned_data

        if get_user_model().objects.filter(email=cd["email"]).exists():
            self.send_password_recovery(cd["username"], cd["email"])
        else:
            self.send_signup_token(cd["username"], cd["email"])

        return super().form_valid(form)

    def send_password_recovery(self, username, email):
        opts = {
            "use_https": self.request.is_secure(),
            "email_template_name": "registration/mail/reset_password.txt",
            "request": self.request,
        }
        logger.info("Sending password recovery mail for '%s' to '%s'", username, email)
        form = ResetPasswordForm({"email": email})
        form.is_valid()
        form.save(**opts)

    def send_signup_token(self, username, email):
        token = make_signup_token(username, email)
        protocol = "https" if self.request.is_secure() else "http"
        domain = self.request.get_host()
        logger.info("Sending signup token mail for '%s' to '%s'", username, email)
        send_template_mail(
            email,
            "registration/mail/signup.txt",
            "Complete your drawpile.net account creation",
            {
                "SIGNUP_URL": protocol
                + "://"
                + domain
                + str(self.success_url)
                + "?token="
                + token,
            },
        )


class FinishSignupView(FormView):
    """Complete the signup and create a new user account.

    Finishing the signup process requires a valid token that
    was generated in the first phase.
    """

    template_name = "registration/finish-signup.html"
    form_class = FinishSignupForm
    success_url = "/"

    def get_initial(self):
        return {"token": self.request.GET.get("token", "")}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            token = self.request.POST.get("token", "")
        else:
            token = self.request.GET.get("token", "")

        if not token:
            ctx["noToken"] = True
        else:
            try:
                ctx["token"] = parse_signup_token(token)
            except ValidationError as e:
                ctx["tokenError"] = e.message

        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = parse_signup_token(cd["token"])

        logger.info("%s (%s) signup complete", token["name"], token["email"])
        with transaction.atomic():
            user = get_user_model().objects.create_user(
                token["name"], token["email"], cd["password"]
            )
            Username.objects.create(user=user, name=token["name"])

        user = authenticate(
            self.request, username=user.username, password=cd["password"]
        )
        login(self.request, user)

        return super().form_valid(form)


class AccountView(LoginRequiredMixin, TemplateView):
    """General account settings"""

    template_name = "users/account.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"profile_page": "account"})
        return ctx

    def post(self, request):
        action = request.POST.get("action", "")
        if action == "change-email":
            print("Changing email")

        return redirect("users:profile-account")


class EmailChangeView(LoginRequiredMixin, FormView):
    """Account email address changing view.
    Like the signup, this is a two-phase process: first, a confirmation
    token is generated and sent to the new email address.
    In the second phase, when the user has proven that they have access
    to the new email address by clicking on the confirmation link,
    the address is actually changed.
    """

    template_name = "users/email_change.html"
    form_class = EmailChangeForm
    success_url = reverse_lazy("users:profile-emailchange-confirm")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"profile_page": "account"})
        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = make_emailchange_token(self.request.user.id, cd["email"])

        protocol = "https" if self.request.is_secure() else "http"
        domain = self.request.get_host()

        logger.info(
            "Sending email change (from %s) confirmation message to %s",
            self.request.user.email,
            cd["email"],
        )
        send_template_mail(
            cd["email"],
            "users/mail/change_email.txt",
            "Changing your drawpile.net account email address",
            {
                "CHANGE_URL": protocol
                + "://"
                + domain
                + str(self.success_url)
                + "?token="
                + token,
            },
        )

        return super().form_valid(form)


class ConfirmEmailChangeView(LoginRequiredMixin, FormView):
    """Change an account's email address.
    This requires the token that was generated in the first phase.
    Additionally, to prevent someone from taking over an account that was
    left logged in, this also requires the current password.
    """

    template_name = "users/email_change_confirm.html"
    form_class = ConfirmEmailChangeForm
    success_url = reverse_lazy("users:profile-account")

    def get_initial(self):
        return {"token": self.request.GET.get("token", "")}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            token = self.request.POST.get("token", "")
        else:
            token = self.request.GET.get("token", "")

        if not token:
            ctx["noToken"] = True
        else:
            try:
                ctx["token"] = parse_emailchange_token(token)
            except ValidationError as e:
                ctx["tokenError"] = e.message

        ctx["profile_page"] = "account"
        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = parse_emailchange_token(cd["token"])

        logger.info("Changing user #%s email to %s", token["user"], token["email"])
        user = get_user_model().objects.get(id=token["user"])
        user.email = token["email"]
        user.save()

        return super().form_valid(form)


class UsernameView(LoginRequiredMixin, TemplateView):
    template_name = "users/usernames.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        mod_status = []
        mod_available = False
        ghost_available = False
        if self.request.user.has_perm("dpauth.moderator"):
            mod_available = True
            if self.request.user.has_perm("dpauth.ghost"):
                mod_status.append("Global moderator and ghost status.")
                ghost_available = True
            else:
                mod_status.append("Global moderator status.")

        memberships = Membership.objects.filter(
            user=self.request.user, status__in=Membership.MOD_STATUSES
        ).select_related("community")

        if len(memberships) > 0:
            mod_available = True
            for m in memberships:
                if m.is_ghost:
                    ghost_available = True
                    what = "Moderator and ghost"
                else:
                    what = "Moderator"
                mod_status.append(f"{what} in {m.community.title}.")

        if mod_available:
            if ghost_available:
                permissions = "MOD,GHOST"
            else:
                permissions = "MOD"
        else:
            permissions = ""

        ctx.update(
            {
                "profile_page": "usernames",
                "max_users": extauth_settings["ALT_COUNT"],
                "mod_status": mod_status,
                "mod_available": mod_available,
                "permissions": permissions,
            }
        )
        return ctx


class DeleteAccountView(LoginRequiredMixin, FormView):
    template_name = "users/delete_account_confirm.html"
    form_class = ConfirmDeleteAccountForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "profile_page": "account",
            }
        )
        return ctx

    def form_valid(self, form):
        user = self.request.user
        logout(self.request)
        logger.info("Deactivating #%d %s (%s)", user.id, user.username, user.email)
        with transaction.atomic():
            user.is_active = False
            user.save()
            try:
                pd = PendingDeletion.objects.get(pk=user.id)
            except PendingDeletion.DoesNotExist:
                pd = PendingDeletion(user_id=user.id)
            pd.deactivated_at = timezone.now()
            pd.save()
        return super().form_valid(form)


class ResetPasswordView(auth_views.PasswordResetView):
    template_name = "registration/reset_password.html"
    email_template_name = "registration/mail/reset_password.txt"
    success_url = reverse_lazy("users:password_reset_done")
    form_class = ResetPasswordForm
