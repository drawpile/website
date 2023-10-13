from django.views.generic import TemplateView
from django.http import Http404
from urllib.parse import quote_plus, urlencode
import re

class InviteView(TemplateView):
    template_name = 'invite.html'
    __PORT_RE = re.compile(r':([0-9]{1,5})')

    def get(self, request, host, port, session, *args, **kwargs):
        url = InviteView.__build_url(host, port, session, request.GET)
        if url:
            return self.render_to_response(self.get_context_data(url=url))
        else:
            raise Http404()

    @staticmethod
    def __build_url(host, port, session, params):
        try:
            port_suffix = InviteView.__parse_port(port)
        except ValueError:
            return None
        return ''.join([
            'drawpile://',
            quote_plus(host, safe=':[]'),
            port_suffix,
            '/',
            quote_plus(session)
        ])

    @staticmethod
    def __parse_port(port):
        if not port:
            return ''

        n = int(port[1:])
        if n < 1 or n > 65535:
            raise ValueError('Port out of bounds')

        return '' if n == 27750 else f':{n}'
