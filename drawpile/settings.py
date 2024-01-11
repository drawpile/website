import os

from .local_settings import *

try:
    # Debug toolbar should not be accidentally enabled when not in debug mode
    DEBUG_TOOLBAR = DEBUG_TOOLBAR and DEBUG
except NameError:
    DEBUG_TOOLBAR = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['drawpile.net', 'localhost']
INTERNAL_IPS = ['127.0.0.1']

if DEBUG:
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'rest_framework',
    'easy_thumbnails',
    'widget_tweaks',
    'corsheaders',

    'dpauth',
    'dpusers',
    'templatepages',
    'news',
    'communities.apps.CommunitiesConfig',
    'invites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dpusers.middleware.UsernameCookieMiddleware',
]

if DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ROOT_URLCONF = 'drawpile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drawpile.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []

AUTHENTICATION_BACKENDS = ['dpusers.backends.EmailOrUsernameModelBackend']

LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files
STATIC_URL = '/media/s/'
STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic', 's')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'allstatic', 'd')
MEDIA_URL = '/media/d/'

THUMBNAIL_BASEDIR = 'thumbnails'

# Email
DEFAULT_FROM_EMAIL = 'no-reply@drawpile.net'
SERVER_EMAIL = 'server@drawpile.net'
EMAIL_SUBJECT_PREFIX = '[drawpile.net] '


# REST API
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# CORS Headers
# Allow requests from the web client.
CORS_ALLOWED_ORIGINS = ["https://web.drawpile.net"]
# Only allow them for the ext-auth endpoint.
CORS_URLS_REGEX = r'^/api/ext-auth/?$'
# And only allow the methods actually required.
CORS_ALLOW_METHODS = ['OPTIONS', 'POST']
