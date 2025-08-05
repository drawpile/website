from django import template
from news.models import Post

register = template.Library()

class NewsNode(template.Node):
    def __init__(self, nodelist, post):
        self.nodelist = nodelist
        self.post = post

    def render(self, context):
        slug = self.post.resolve(context)

        if slug == '_latest':
            latest = True
            try:
                post = Post.objects.visible()[0]
            except IndexError:
                post = None
        else:
            latest = False
            try:
                post = Post.objects.visible().get(slug=slug)
            except Post.DoesNotExist:
                post = None

        context.push()
        context['post'] = post
        context['post_latest'] = latest
        out = self.nodelist.render(context)
        context.pop()
        return out

    def __repr__(self):
        return '<News node: {0}>'.format(self.image)

@register.tag
def news_article(parser, token):
    try:
        tag_name, post_slug = token.split_contents()
        nodelist = parser.parse(('endnews_article',))
        parser.delete_first_token()
    except ValueError:
        raise template.TemplateSyntaxError("news_article tag requires a single argument")

    return NewsNode(nodelist, parser.compile_filter(post_slug))

