from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import transaction

from dpauth.models import Username
from dpauth.settings import extauth_settings
from .forms import (
    SignupForm, FinishSignupForm, EmailChangeForm,
    ConfirmEmailChangeForm, ConfirmDeleteAccountForm
    )
from .token import (
    make_signup_token, parse_signup_token,
    make_emailchange_token, parse_emailchange_token
    )
from .mail import send_template_mail
from .deletion import get_cascade_deletion_list

class SignupView(FormView):
    """New user signup: first phase.

    This doesn't save anything in the database yet. Instead, it generates
    a token for the next phase, which actually creates the account.
    The token is mailed to the given email address to ensure the
    address is real.

    If the email address is registered already, a password recovery mail is
    sent instead.
    """
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:finish-signup')

    def form_valid(self, form):
        cd = form.cleaned_data

        if get_user_model().objects.filter(email=cd['email']).exists():
            self.send_password_recovery(cd['email'])
        else:
            self.send_signup_token(cd['username'], cd['email'])

        return super().form_valid(form)

    def send_password_recovery(self, email):
        opts = {
            'use_https': self.request.is_secure(),
            'email_template_name': 'registration/mail/reset_password.txt',
            'request': self.request,
        }
        form = PasswordResetForm({'email': email})
        form.is_valid()
        form.save(**opts)

    def send_signup_token(self, username, email):
        token = make_signup_token(username, email)
        protocol = 'https' if self.request.is_secure() else 'http'
        domain = self.request.get_host()
        send_template_mail(
            email,
            'registration/mail/signup.txt',
            'Complete your drawpile.net account creation',
            {
                'SIGNUP_URL': protocol + '://' + domain + str(self.success_url) + '?token=' + token,
            }
        )


class FinishSignupView(FormView):
    """Complete the signup and create a new user account.

    Finishing the signup process requires a valid token that
    was generated in the first phase.
    """
    template_name = 'registration/finish-signup.html'
    form_class = FinishSignupForm
    success_url = '/'

    def get_initial(self):
        return {
            'token': self.request.GET.get('token', '')
        }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            token = self.request.POST.get('token', '')
        else:
            token = self.request.GET.get('token', '')

        if not token:
            ctx['noToken'] = True
        else:
            try:
                ctx['token'] = parse_signup_token(token)
            except ValidationError as e:
                ctx['tokenError'] = e.message

        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = parse_signup_token(cd['token'])

        with transaction.atomic():
            user = get_user_model().objects.create_user(
                token['name'],
                token['email'],
                cd['password']
                )
            Username.objects.create(
                user=user,
                name=token['name']
                )

        user = authenticate(self.request, username=user.username, password=cd['password'])
        login(self.request, user)

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    """General account settings"""

    template_name = 'users/account.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'profile_page': 'account'
        })
        return ctx

    def post(self, request):
        action = request.POST.get('action', '')
        if action == 'change-email':
            print ("Changing email")

        return redirect('users:profile-account')


@method_decorator(login_required, name='dispatch')
class EmailChangeView(FormView):
    """Account email address changing view.
    Like the signup, this is a two-phase process: first, a confirmation
    token is generated and sent to the new email address.
    In the second phase, when the user has proven that they have access
    to the new email address by clicking on the confirmation link,
    the address is actually changed.
    """

    template_name = 'users/email_change.html'
    form_class = EmailChangeForm
    success_url = reverse_lazy('users:profile-emailchange-confirm')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'profile_page': 'account'
        })
        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = make_emailchange_token(self.request.user.id, cd['email'])

        protocol = 'https' if self.request.is_secure() else 'http'
        domain = self.request.get_host()

        send_template_mail(
            cd['email'],
            'users/mail/change_email.txt',
            'Changing your drawpile.net account email address',
            {
                'CHANGE_URL': protocol + '://' + domain + str(self.success_url) + '?token=' + token,
            }
        )

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ConfirmEmailChangeView(FormView):
    """Change an account's email address.
    This requires the token that was generated in the first phase.
    Additionally, to prevent someone from taking over an account that was
    left logged in, this also requires the current password.
    """

    template_name = 'users/email_change_confirm.html'
    form_class = ConfirmEmailChangeForm
    success_url = reverse_lazy('users:profile-account')

    def get_initial(self):
        return {
            'token': self.request.GET.get('token', '')
        }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            token = self.request.POST.get('token', '')
        else:
            token = self.request.GET.get('token', '')

        if not token:
            ctx['noToken'] = True
        else:
            try:
                ctx['token'] = parse_emailchange_token(token)
            except ValidationError as e:
                ctx['tokenError'] = e.message

        ctx['profile_page'] = 'account'
        return ctx

    def form_valid(self, form):
        cd = form.cleaned_data
        token = parse_emailchange_token(cd['token'])

        get_user_model().objects.filter(id=token['user']).update(email=token['email'])

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UsernameView(TemplateView):
    template_name = 'users/usernames.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        usernames = list(Username.objects.filter(user=self.request.user))
        usernames.sort(key=lambda x: -1 if x.name == self.request.user.username
        else 0)

        ctx.update({
            'profile_page': 'usernames',
            'usernames': usernames,
            'can_add': len(usernames) < extauth_settings['ALT_COUNT'],
        })
        return ctx

    def post(self, request, *args, **kwargs):
        action, target = request.POST['action'].split('-')
        ctx = self.get_context_data(**kwargs)
        names = {n.id: n for n in ctx['usernames']}

        if action == 'add':
            if ctx['can_add']:
                new_name = Username(
                    user=request.user,
                    name=request.POST['username']
                    )
                try:
                    new_name.full_clean()
                except ValidationError as e:
                    ctx['name_error'] = ' '.join(e.messages)
                    ctx['new_username'] = request.POST['username']
                    return self.render_to_response(ctx)

                new_name.save()

        elif action == 'primary':
            request.user.username = names[int(target)].name
            request.user.save(update_fields=('username',))

        elif action == 'remove':
            names[int(target)].delete()

        elif action == 'mod':
            name = names[int(target)]
            name.is_mod = not name.is_mod
            name.save(update_fields=('is_mod',))

        return redirect('users:profile-usernames')

@method_decorator(login_required, name='dispatch')
class DeleteAccountView(FormView):
    template_name = 'users/delete_account_confirm.html'
    form_class = ConfirmDeleteAccountForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'profile_page': 'account',
            'tbd': get_cascade_deletion_list(self.request.user),
        })
        return ctx

    def form_valid(self, form):
        user = self.request.user
        logout(self.request)
        user.delete()
        return super().form_valid(form)

