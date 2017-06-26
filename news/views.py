from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models

class NewsListView(ListView):
    paginate_by=5

    def get_queryset(self):
        return models.Post.objects.visible()


class NewsDetailView(DetailView):
    def get_queryset(self):
        return models.Post.objects.visible()

