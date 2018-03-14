from django import template
from django.utils.safestring import mark_safe
from django.utils import html

register = template.Library()

@register.filter(name='safetext')
def safetext_filter(text):
    return mark_safe(
        html.urlize(
            html.linebreaks(text, True),
            nofollow=True
        )
    )
