from django import template
from django.utils.html import format_html, escape
from django.conf import settings

from templatepages.models import Image, TemplateVar

register = template.Library()

@register.simple_tag(takes_context=True)
def navilink(context, url, title, classes=''):
    """Usage:

    {% navilink '/news/ 'News' classes='nav-item' %}

    The class 'is-active' is added to a link when the current request
    path starts with the link path.
    """

    if context.request.path.startswith(url):
        classes = classes + ' is-active'

    return format_html('<a class="{classes}" href="{url}">{title}</a>',
        url=url,
        title=escape(title),
        classes=classes,
    )


@register.simple_tag()
def templatevar(name):
    """Usage:

    Current version is {% templatevar 'VERSION' %}.
    {% templatevar 'VERSION' as version %}
    Current version is {{ version }}.
    """
    try:
        return TemplateVar.objects.get(name=name).text
    except TemplateVar.DoesNotExist:
        return '(' + name + ' not set)' if settings.DEBUG else ''


class ImageNode(template.Node):
    def __init__(self, nodelist, image):
        self.nodelist = nodelist
        self.image = image

    def render(self, context):
        imagename = self.image.resolve(context)

        context.push()

        try:
            context['image'] = Image.objects.get(name=imagename)
        except Image.DoesNotExist:
            context['image'] = None

        out = self.nodelist.render(context)

        context.pop()

        return out

    def __repr__(self):
        return '<Image node: {0}>'.format(self.image)


@register.tag
def image(parser, token):
    """Usage:

    {% image "name" %}
        <img src="{{ image.image.url }}" alt="{{ image.alt_text }}">
    {% endimage %}
    """
    try:
        tag_name, image_name = token.split_contents()
        nodelist = parser.parse(('endimage',))
        parser.delete_first_token()
    except ValueError:
        raise template.TemplateSyntaxError("image tag requires a single argument")

    return ImageNode(nodelist, parser.compile_filter(image_name))

