from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView
import logging
import subprocess
from .forms import AuthUsernamesForm, MonitorRestartForm
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

    def get(self, request, *args, **kwargs):
        name = request.GET.get("name")
        if name and request.user.drawpilename_set.filter(name=name).exists():
            return redirect("auth:finish", name)
        else:
            return super().get(request, *args, **kwargs)

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


class MonitorManagerView(PermissionRequiredMixin, TemplateView):
    template_name = "monitor_manager.html"
    permission_required = "dpauth.view_monitorwordlist"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        command = settings.DRAWPILE_MONITOR_STATUS_COMMAND
        if not command:
            raise ValueError("DRAWPILE_MONITOR_STATUS_COMMAND not configured")
        logger.info(
            "Checking drawpile-monitor status at the behest of %s (%d): %s",
            user.username,
            user.id,
            command,
        )
        process = subprocess.run(
            command,
            timeout=5,
            encoding="UTF-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        ctx.update(
            {
                "status_returncode": process.returncode,
                "status_stdout": process.stdout,
                "can_restart": user.has_perm("dpauth.change_monitorwordlist",)
            }
        )
        return ctx


class MonitorManagerRestartView(PermissionRequiredMixin, FormView):
    permission_required = "dpauth.change_monitorwordlist"
    form_class = MonitorRestartForm

    def get_success_url(self):
        return reverse("auth:monitor-manager")

    def form_valid(self, form):
        user = self.request.user
        command = settings.DRAWPILE_MONITOR_RELOAD_COMMAND
        if not command:
            raise ValueError("DRAWPILE_MONITOR_RELOAD_COMMAND not configured")
        logger.info(
            "Restarting drawpile-monitor at the behest of %s (%d): %s",
            user.username,
            user.id,
            command,
        )
        process = subprocess.run(
            command,
            timeout=5,
            encoding="UTF-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        logger.info(
            "Restarted drawpile-monitor result %d: %s",
            process.returncode,
            process.stdout,
        )
        if process.returncode == 0:
            messages.success(self.request, "Restarted drawpile-monitor successfully.")
        else:
            messages.error(
                self.request,
                f"Restart exited with {process.returncode}, check logs for details.",
            )
        return super().form_valid(form)
