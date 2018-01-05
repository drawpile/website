from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import IntegrityError

from base64 import b64encode

import ed25519
import sys

class Command(BaseCommand):
    help = 'Manage Drawpile External Authentication'

    #def add_arguments(self, parser):
        #parser.add_argument('action', type=str)

    def handle(self, *args, **kwargs):
        self.make_keypair()

        #if kwargs['action'] == 'make_keypair':
        #    self.make_keypair()
        #else:
        #    raise CommandError("Unsupported action")

    def make_keypair(self):
        priv, pub = ed25519.create_keypair()

        print (r"""# Ext auth key pair. Place this in local_settings.py
DRAWPILE_EXT_AUTH = {{
    'PRIVATE_KEY': b64decode({priv}),
    'PUBLIC_KEY': b64decode({pub}),
}}""".format(
            priv=b64encode(priv.to_bytes()),
            pub=b64encode(pub.to_bytes())
        ))

