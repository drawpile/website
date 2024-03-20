from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import FormView, TemplateView
import logging
from .forms import AuthUsernamesForm
from .models import Username

logger = logging.getLogger(__name__)


class AuthLoginView(LoginView):
    redirect_authenticated_user = True
    next_page = "auth:usernames"
    redirect_field_name = None
    template_name = "auth_login.html"

    def get_success_url(self):
        return reverse("auth:usernames")


class AuthLogoutView(LogoutView):
    redirect_authenticated_user = True
    next_page = "auth:login"
    redirect_field_name = None

    def get_success_url(self):
        return reverse("auth:login")


class AuthUsernamesView(LoginRequiredMixin, FormView):
    form_class = AuthUsernamesForm
    login_url = "auth:login"
    redirect_field_name = None
    template_name = "auth_usernames.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "usernames": list(self.request.user.drawpilename_set.all()),
            }
        )
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        name = form.cleaned_data["username"]
        self.success_url = reverse("auth:finish", args=[name])
        return super().form_valid(form)


class AuthFinishView(LoginRequiredMixin, TemplateView):
    template_name = "auth_finish.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "frame_ancestors": settings.DRAWPILE_AUTH_FRAME_ANCESTORS,
            }
        )
        return ctx


class BanAnalyzerView(PermissionRequiredMixin, TemplateView):
    template_name = "ban_analyzer.html"
    permission_required = "dpauth.change_ban"
