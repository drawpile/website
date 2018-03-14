from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from gallery.models import Group, Submission, Picture

import os

class Command(BaseCommand):
    """Usage:
    manage.py media <action> [--model modelname,...]

    Supported actions:

    missing - list missing files
    clean   - clean orphaned files
    dedupe  - remove duplicate uploads
    """

    help = 'Manage content addressed file uploads'

    MODELS = [
        {
            'model': Submission,
            'fields': ['thumbnail'],
        },
        {
            'model': Picture,
            'fields': ['downscaled', 'fullsize'],
        },
        {
            'model': Group,
            'fields': ['logo'],
        },
    ]

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        parser.add_argument('models', nargs='*')
        parser.add_argument('--dry-run', action='store_true', dest='dryrun')

    def handle(self, *args, **kwargs):
        action = kwargs['action']
        self.dryrun = kwargs['dryrun']
        self.verbosity = int(kwargs['verbosity']) if not self.dryrun else 3
        self.limit_models = kwargs['models']

        if not action:
            raise CommandError('No action given')
        if action == 'clean':
            self.handle_model_action(self.clean_field, 'Cleaning')
        elif action == 'dedupe':
            self.handle_model_action(self.dedupe_field, 'Deduplicating')
        elif action == 'missing':
            self.handle_model_action(self.missing_field, 'Finding missing files')
        else:
            raise CommandError('Unknown action: ' + action)

    def handle_model_action(self, action, verb):
        for model in self.MODELS:
            if self.limit_models and model['model'].__name__ not in self.limit_models:
                continue
            if self.verbosity > 2:
                print ("{} {}...".format(verb, model['model'].__name__))

            for field in model['fields']:
                if isinstance(field, str):
                    action(model['model'], {'name': field})
                else:
                    action(model['model'], field)

    def field_dir(self, modelcls, field):
        """Return the field's root directory."""
        if 'dir' in field:
            return field['dir']

        upload_to = getattr(modelcls, field['name']).field.upload_to
        if hasattr(upload_to, 'basepath'):
            return upload_to.basepath

        return upload_to

    def clean_field(self, modelcls, field):
        """Delete all unreferenced files from the field upload directories.
        Note: this assumes the directory is used only for that field!
        """
        paths = modelcls.objects.exclude(**{field['name']: ''}).values_list(field['name'], flat=True)
        root = self.field_dir(modelcls, field)

        # Sanity check
        for p in paths:
            if not p.startswith(root):
                raise CommandError("Field {field} of model {model} has a file outside the usual root path!".format(
                    field=field['name'],
                    model=modelcls.__name__
                    ))

        filenames = set(p[len(root):] for p in paths)
        
        for f in os.listdir(os.path.join(settings.MEDIA_ROOT, root)):
            if f not in filenames:
                if self.verbosity > 1:
                    print ("Unreferenced file:", f)
                if not self.dryrun:
                    os.remove(os.path.join(settings.MEDIA_ROOT, root, f))

    def dedupe_field(self, modelcls, field):
        """Remove duplicate files.
        Note: assumes file naming scheme is <basedir>/<hash>[_random][.ext]
        The '_' character should not appear in the hash
        """
        paths = modelcls.objects.filter(**{field['name'] + '__contains': '_'}).values_list('pk', field['name'])
        root = self.field_dir(modelcls, field)

        for id, p in paths:
            # Sanity check
            if not p.startswith(root):
                raise CommandError("Field {field} of model {model} has a file outside the usual root path!".format(
                    field['name'], modelcls.__name__))

            filename = p[len(root):]
            if '.' in filename:
                ext = filename[filename.index('.'):]
                filename = filename.split('.', 1)[0]
            else:
                ext = ''

            if '_' in filename:
                if self.verbosity > 1:
                    print("Duplicate file:", p)

                # Check that the original still exists
                original = os.path.join(root, filename[:filename.index('_')] + ext)

                if os.path.exists(os.path.join(settings.MEDIA_ROOT, original)):
                    # Good, remove the duplicate and update the reference
                    if self.verbosity > 2:
                        print("Deleting", p)
                    if not self.dryrun:
                        os.remove(os.path.join(settings.MEDIA_ROOT, p))

                else:
                    # Uh oh, it's gone missing? Rename this file
                    # and update the reference
                    if self.verbosity > 2:
                        print("Renaming", p)
                    if not self.dryrun:
                        os.rename(
                            os.path.join(settings.MEDIA_ROOT, p),
                            os.path.join(settings.MEDIA_ROOT, original)
                            )

                if not self.dryrun:
                    modelcls.objects.filter(pk=id).update(**{field['name']: original})

    def missing_field(self, modelcls, field):
        """List all model/field instances where the file is missing."""
        paths = modelcls.objects.all().values_list('pk', field['name'])
        root = self.field_dir(modelcls, field)

        for id, p in paths:
            if not p:
                continue

            if not p.startswith(root):
                print("{model}.{field} #{id} wrong root path: {path} (should be {root})".format(
                    model=modelcls.__name__,
                    field=field['name'],
                    id=id,
                    path=p,
                    root=root
                    ))

            if not os.path.exists(os.path.join(settings.MEDIA_ROOT, p)):
                print("{model}.{field} #{id} missing: {path}".format(
                    model=modelcls.__name__,
                    field=field['name'],
                    id=id,
                    path=p
                    ))

