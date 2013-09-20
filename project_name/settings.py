import os
import dj_database_url
# Django settings for {{project_name}} project.

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(PROJECT_DIR, '../assets')
LOG_DIR = os.path.join(PROJECT_DIR, '../logs')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nick Pack', 'nick@nickpack.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config()
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(ASSETS_DIR, '/media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ASSETS_DIR, '/static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ASSETS_DIR, '/static/base-templates')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

FIXTURE_DIRS = (os.path.join(PROJECT_DIR, '../fixtures'))

SECRET_KEY = r"{{ secret_key }}"

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = '{{project_name}}.urls'

WSGI_APPLICATION = '{{project_name}}.wsgi.application'

TEMPLATE_DIRS = (

)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin'
)

THIRD_PARTY_APPS = (
    'south',
)

LOCAL_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] "
                      "%(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + "django.log",
            'maxBytes': 6291456,
            'backupCount': 7,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
