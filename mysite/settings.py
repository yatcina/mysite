"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1#pp*o54@@7h_z*0_(kzs4iyl%rxunp*)*_g6j7yr_ulm6jwf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    '../mysite/templates',
    '../mysite/templates/sites', # Change this to your own directory.
)

ALLOWED_HOSTS = []
#E-mail
EMAIL_HOST = '10.0.0.9'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'yatcina@mebtorg.ru'
EMAIL_HOST_PASSWORD = 'Cjcbcj4yfz'
DEFAULT_FROM_EMAIL = 'yatcina@mebtorg.ru'
SERVER_EMAIL = 'yatcina@mebtorg.ru'
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location


# Application definition

INSTALLED_APPS = (
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'books',
    'rabota',
    'sites',
    'googlecharts',
    'registration',
)
AUTH_PROFILE_MODULE = 'sites.UserProfile'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
SITE_ID = 2
ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
		'USER': 'root',
		'PASSWORD': 123,
		'HOST': 'localhost',
		'PORT': '3306',
    }
}

LOCALE_PATHS = (
    'sites/locale',
    # os.path.join(PROJECT_DIR, 'locale'),
)

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
def lef(*x):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), *x).replace('\\','/'))

STATICFILES_DIRS = (

    '../mysite/statics/',
)
MEDIA_ROOT = lef('../tmp/')
MEDIA_URL = 'http://10.0.254.56:8000/'
STATIC_ROOT = lef('../statics/')
STATIC_URL = 'http://10.0.254.56:8000/statics/'

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_STATIC_ROOT = STATIC_ROOT
FILEBROWSER_STATIC_URL = STATIC_URL
URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'
PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'
LOGIN_REDIRECT_URL = '/rabota/'

ACCOUNT_ACTIVATION_DAYS = 2
PASSWORD_RESET_TIMEOUT_DAYS = 2




