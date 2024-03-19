from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.template.exceptions import TemplateDoesNotExist
from django.http import Http404


class TemplatePageResponse(TemplateResponse):
    def resolve_template(self, template):
        try:
            return super().resolve_template(template)
        except TemplateDoesNotExist:
            raise Http404


class TemplatePageView(TemplateView):
    response_class = TemplatePageResponse
    template_root = "pages/"

    def get_template_names(self):
        path = self.kwargs["path"]

        if path and path[-1] == "/":
            path = path[:-1]

        if not path:
            return (self.template_root + "index.html",)

        for c in path:
            if not c.isalnum() and c not in "/-.":
                raise Http404

        return (
            self.template_root + path + ".html",
            self.template_root + path + "/index.html",
        )
