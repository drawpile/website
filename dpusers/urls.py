from django.conf import settings
from django.views.generic import RedirectView, TemplateView
from django.urls import reverse_lazy
from django.urls import path, re_path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    path('tos/', TemplateView.as_view(template_name='registration/tos.html'), name='tos'),
]

if settings.DRAWPILE_READONLY_SITE:
    urlpatterns += [
        re_path(r'.*', RedirectView.as_view(url='/readonly/', permanent=False)),
    ]
else:
    urlpatterns += [
        path('signup/', views.SignupView.as_view(), name='signup'),
        path('finish-signup/', views.FinishSignupView.as_view(), name='finish-signup'),

        path('profile/', views.AccountView.as_view(), name='profile-account'),
        path('profile/email_change/', views.EmailChangeView.as_view(), name='profile-emailchange'),
        path('profile/email_change/confirm/', views.ConfirmEmailChangeView.as_view(), name='profile-emailchange-confirm'),
        path('profile/usernames/', views.UsernameView.as_view(), name='profile-usernames'),

        path('delete/', views.DeleteAccountView.as_view(), name='delete-account'),

        # Views provided by Django:
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),

        path(
            'profile/password_change/',
            auth_views.PasswordChangeView.as_view(
                template_name='users/password_change.html',
                success_url=reverse_lazy('users:password_change_done'),
                extra_context={'profile_page': 'password_change'}
            ),
            name='password_change'
        ),
        path(
            'profile/password_change/done/',
            auth_views.PasswordChangeDoneView.as_view(
                template_name='users/password_change_done.html',
                extra_context={'profile_page': 'password_change'}
                ),
            name='password_change_done'
        ),
        path(
            'password_reset/',
            views.ResetPasswordView.as_view(),
            name='password_reset'
        ),
        path(
            'password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='registration/reset_password_done.html'
            ),
            name='password_reset_done'
        ),
        path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='registration/reset_password_confirm.html',
                success_url=reverse_lazy('users:password_reset_complete')
            ),
            name='password_reset_confirm'
        ),
        path(
            'reset/done/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='registration/reset_password_complete.html'
            ),
            name='password_reset_complete'
        ),
    ]

