from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings

def send_template_mail(recipient, template, title, context):
    """Send an email using a template to the given user.

    Parameters:
    user     - the recipient address
    template - name of the Django template to use
    title    - message title
    context  - template context variables (dict)
    """

    tpl = get_template(template)

    body = tpl.render(context)
    
    send_mail(
        title,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [recipient]
        )

