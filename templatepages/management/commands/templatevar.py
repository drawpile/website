from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import IntegrityError
from django.core.files import File
from django.conf import settings

from templatepages.models import TemplateVar

import os

class Command(BaseCommand):
    help = 'Set or read template variables'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, nargs='?')
        parser.add_argument('value', type=str, nargs='*')
        parser.add_argument('--no-overwrite',
            action='store_false', dest='overwrite', default=True,
            help="Don't set the value if it exists and is not empty"
        )

    def handle(self, *args, **kwargs):
        if not kwargs['name']:
            # No name given: list all variables
            for var in TemplateVar.objects.all():
                print('{}: {}'.format(var.name, var.text))

        elif not kwargs['value']:
            # No value given: show variable
            try:
                print(TemplateVar.objects.get(name=kwargs['name']).text)
            except TemplateVar.DoesNotExist:
                pass

        else:
            # Value given: set variable
            value = ' '.join(kwargs['value'])
            obj, created = TemplateVar.objects.get_or_create(
                name=kwargs['name'],
                defaults={'text': value}
                )
            if not created and kwargs['overwrite']:
                obj.text = value
                obj.save()

