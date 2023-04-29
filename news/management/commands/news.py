from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import IntegrityError

from news.models import Post

import sys

class Command(BaseCommand):
    help = 'Import/export news articles'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        parser.add_argument('target', type=str)
        parser.add_argument('--overwrite',
            action='store_true', dest='overwrite', default=False,
            help='Overwrite existing post on import'
        )
        parser.add_argument('--to-file',
            action='store_true', dest='tofile', default=False,
            help='Export article to <slug>.txt'
        )

    def handle(self, *args, **kwargs):
        if kwargs['action'] == 'import':
            self.import_article(kwargs['target'], overwrite=kwargs['overwrite'])

        elif kwargs['action'] == 'export':
            self.export_article(kwargs['target'], to_file=kwargs['tofile'])

        else:
            raise CommandError("Action must be either import or export")

    def export_article(self, slug, to_file=False):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise CommandError("Post '" + slug + '" not found.')

        if to_file:
            with open(slug + '.txt', 'w') as f:
                self.__export_article(post, f)

        else:
            self.__export_article(post, sys.stdout)

    def __export_article(self, post, out):
        print("Slug:", post.slug, file=out)
        print("Title:", post.title, file=out)
        print("Publish:", post.publish, file=out)
        print("Visible:", post.is_visible, file=out)
        print("Author:", post.author_name, file=out)
        print("---", file=out)
        print(post.intro, file=out)
        print("---", file=out)
        print(post.readmore, file=out)

    def import_article(self, filename, overwrite=False):
        with open(filename, 'r') as f:
            section = 0
            metadata = {}
            sections = [[], []]
            for line in f:
                line = line.rstrip()
                if line == '---' and section < 2:
                    section += 1
                    continue

                if section == 0:
                    # Metadata section
                    try:
                        key, value = [x.strip() for x in line.split(':', 1)]
                    except ValueError:
                        raise CommandError("Invalid metadata key:value pair: " + line)

                    metadata[key.lower()] = value

                else:
                    # Intro and readmore sections
                    sections[section-1].append(line)

            try:
                post = Post(
                    slug=metadata['slug'],
                    publish=metadata.get('publish', timezone.now()),
                    is_visible=metadata.get('visible', 'true').lower() == 'true',
                    title=metadata['title'],
                    author_name=metadata['author'],
                    intro='\n'.join(sections[0]),
                    readmore='\n'.join(sections[1]),
                    )
            except KeyError as ke:
                raise CommandError("Metadata field " + ke.args[0] + " is required.")

            try:
                post.save()
            except IntegrityError:
                if not overwrite:
                    raise CommandError("Article exists. Use --overwrite to update.")

                post.id = Post.objects.filter(slug=post.slug).values_list('id', flat=True)[0]
                post.save()

