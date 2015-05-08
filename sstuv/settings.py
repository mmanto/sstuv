"""
Django settings for sstuv project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.urls.static import static
from django.conf import settings
from django.conf.global_settings import STATIC_ROOT

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT
SITE_ID = int(os.environ.get("SITE_ID", 1))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z_r1^nfp35alwa7g-qv%zym0b$@xh46nfhs%xh0+2z3fn72*3y'

# SECURITY WARNING: don't run with debug turned on in production!


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "django.contrib.sites",
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'rest_framework',
    'wkhtmltopdf', 
    'comun', 
    'documentos', 
    'publicador', 
    'procesos',
    'secur',
    'regularizacion'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sstuv.urls'

WSGI_APPLICATION = 'sstuv.wsgi.application'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    #"account.context_processors.account",
    #"pinax_theme_bootstrap.context_processors.theme",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'fileInfo': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/sstuv/log/info.log',
            'formatter': 'verbose'
        },
        'fileError': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/sstuv/log/error.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['fileInfo'],
            'propagate': True,
            'level':'INFO',
        },
        'sstuvInfo': {
            'handlers': ['fileInfo'],
            'propagate': True,
            'level': 'INFO',
        },
        'sstuvError': {
            'handlers': ['fileError'],
            'propagate': True,
            'level': 'ERROR',
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = '/home/avazzano/git/sstuv/sstuv/static'

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'SSTUV',
            'USER': 'postgres',
	        'PASSWORD': 'postgres',
	        'HOST': 'localhost',
	        'PORT': '',                      # Set to empty string for default.
    },
    'legacy': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'SIG_DESA',
            'USER':'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '',
    }
}

#DATABASE_ROUTERS = ['comun.Integration_router.IntegrationRouter']


# url to redirect after successfull login
LOGIN_REDIRECT_URL = '/sig/expedientes'
LOGIN_URL='/admin/login/'

WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'


