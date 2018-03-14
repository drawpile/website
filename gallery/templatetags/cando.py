from django import template

register = template.Library()

@register.filter(name='can')
def if_can(obj, user):
    return (obj, user)

@register.filter(name='use')
def can_use(obj, action):
    return getattr(obj[0], 'can_' + action)(obj[1])

