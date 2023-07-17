from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.urls import reverse_lazy
from dpauth.models import Username
from dpusers.token import make_signup_token

class Command(BaseCommand):
    help = 'Get a registration confirmation link'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']

        username_taken = Username.exists(username)
        email_taken = get_user_model().objects.filter(email=email).exists()
        if username_taken and email_taken:
            raise CommandError("Username and email are already taken")
        elif username_taken:
            raise CommandError("Username is already taken")
        elif email_taken:
            raise CommandError("Email is already taken")

        token = make_signup_token(username, email)
        success_url = reverse_lazy('users:finish-signup')

        print()
        print(f'Send the text below the line to {email}')
        print()
        print('DO NOT HAND IT TO THEM IN ANY OTHER WAY!')
        print()
        print('Only through email. We must be sure they own that address.')
        print()
        print('------------------------------')
        print()
        print("Hi, since your email provider doesn't accept emails from drawpile.net, I'm sending you the registration link manually.")
        print()
        print(f'https://drawpile.net{success_url}?token={token}')
        print()
        print("If you didn't ask to sign up for Drawpile, please let me know. That means someone is impersonating you.")
        print()
        print("Best regards from the Drawpile administration.")
        print()
