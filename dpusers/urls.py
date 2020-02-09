from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^finish-signup/$', views.FinishSignupView.as_view(), name='finish-signup'),
    url(r'^tos/$', TemplateView.as_view(template_name='registration/tos.html'), name='tos'),

    url(r'^profile/$', views.AccountView.as_view(), name='profile-account'),
    url(r'^profile/email_change/$', views.EmailChangeView.as_view(), name='profile-emailchange'),
    url(r'^profile/email_change/confirm/$', views.ConfirmEmailChangeView.as_view(), name='profile-emailchange-confirm'),
    url(r'^profile/usernames/$', views.UsernameView.as_view(), name='profile-usernames'),

    url(r'^delete/$', views.DeleteAccountView.as_view(), name='delete-account'),

    # Views provided by Django:
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(
        r'^profile/password_change/$',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url=reverse_lazy('users:password_change_done'),
            extra_context={'profile_page': 'password_change'}
        ),
        name='password_change'
    ),
    url(
        r'^profile/password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
            extra_context={'profile_page': 'password_change'}
            ),
        name='password_change_done'
    ),

    url(
        r'^password_reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='registration/reset_password.html',
            email_template_name='registration/mail/reset_password.txt',
            success_url=reverse_lazy('users:password_reset_done')
        ),
        name='password_reset'
    ),
    url(
        r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/reset_password_done.html'
        ),
        name='password_reset_done'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/reset_password_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/reset_password_complete.html'
        ),
        name='password_reset_complete'
    ),
]

