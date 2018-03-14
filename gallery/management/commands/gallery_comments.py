from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from gallery.models import Comment

from datetime import timedelta

class Command(BaseCommand):
    """Usage:
    
    manage.py gallery_comments <action> [--days <days>]
    
    Supported actions:
    purge - permanently delete comments
    """
    help = 'Manage gallery comments'
    
    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        parser.add_argument('--days', type=int, default=1)
        parser.add_argument('--dry-run', action='store_true', dest='dryrun')

    def handle(self, *args, **kwargs):
        action = kwargs['action']
        
        self.dryrun = kwargs['dryrun']
        self.verbosity = int(kwargs['verbosity']) if not self.dryrun else 3
        
        if not action:
            raise CommandError('No action given')
        
        if action == 'purge':
            self.__purge(kwargs['days'])
        else:
            raise CommandError("Unknown action: " + action)
    
    def __purge(self, days):
        cutoff = timezone.now() - timedelta(days=days)
        qs = Comment.objects.filter(deleted__lte=cutoff)
        
        if self.verbosity > 1:
            print("Purging %d comments deleted at least %d day(s) ago..." % (qs.count(), days))
        
        if not self.dryrun:
            qs.delete()
