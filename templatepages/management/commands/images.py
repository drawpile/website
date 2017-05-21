from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import IntegrityError
from django.core.files import File
from django.conf import settings

from templatepages.models import Image

import os

class Command(BaseCommand):
    help = 'Manage uploaded images that are used in static/semi-static pages'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        parser.add_argument('filename', type=str, nargs='*')
        parser.add_argument('--alt', type=str, dest='alt_text')
        parser.add_argument('--overwrite',
            action='store_true', dest='overwrite', default=False,
            help='Overwrite existing post on import'
        )

    def handle(self, *args, **kwargs):
        if kwargs['action'] == 'add':
            for fn in kwargs['filename']:
                self.add_image(fn,
                    alt_text=kwargs.get('alt_text', ''),
                    overwrite=kwargs['overwrite']
                    )
        elif kwargs['action'] == 'cleanup':
            if len(kwargs['filename']) > 0:
                raise CommandError("cleanup command takes no arguments.")

            self.cleanup()
        else:
            raise CommandError("Unknown action. Must be either add or cleanup")

    def add_image(self, srcfile, alt_text='', overwrite=False):
        # First, check if the file already exists in image library
        filename = srcfile
        if '/' in filename:
            filename = filename[filename.rindex('/')+1:]

        try:
            img = Image.objects.get(name=filename)
        except Image.DoesNotExist:
            img = Image(name=filename)
        else:
            if not overwrite:
                raise CommandError(filename + ": already exists")

        if alt_text:
            img.alt_text = alt_text

        with open(srcfile, 'rb') as f:
            img.image = File(f, filename)
            img.save()

    def cleanup(self):
        IMAGEDIR = 'images/'
        known_images = set(Image.objects.all().values_list('image', flat=True))
        print(known_images)
        removed = 0
        for f in os.listdir(os.path.join(settings.MEDIA_ROOT, IMAGEDIR)):
            if IMAGEDIR+f not in known_images:
                removed += 1
                print ("Removing unreferenced image:", f)
                os.remove(os.path.join(settings.MEDIA_ROOT, IMAGEDIR, f))
        
        print("Removed %d unreferenced images (leaving %d known images)" % (removed, len(known_images)))

