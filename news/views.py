from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from . import models

from commonmark import commonmark


class NewsListView(ListView):
    paginate_by=5

    def get_queryset(self):
        return models.Post.objects.visible()


class NewsDetailView(DetailView):
    def get_queryset(self):
        qs = models.Post.objects
        if not self.request.user.has_perm('news.change_post'):
            qs = qs.visible()
        else:
            qs = qs.all()
        return qs


class NewsFeed(Feed):
    feed_type = Atom1Feed
    title = "Drawpile.net news"
    link = '/news/'

    def items(self):
        return models.Post.objects.visible()[:5]

    def item_title(self, item):
        return item.title

    def item_author_name(self):
        return "Drawpile.net"

    def item_description(self, item):
        return commonmark(item.intro)

    def item_pubdate(self, item):
        return item.publish
