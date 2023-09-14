"""
Django settings for itinerari project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
MAIN_APP_DIR = Path(__file__).resolve().parent
BASE_DIR = MAIN_APP_DIR.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m%=+vp%7a44le-(2f^zv97j3&963cn#dgy5e^(o67h91_5j)+a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "192.168.1.101",
    "casalorenzo.ddns.net"
]


# Application definition

INSTALLED_APPS = [
    'django_google_fonts',
    'schedule',
    'djangobower',
    'leaflet',
    'loader.apps.LoaderConfig',
    'latex_generator.apps.LatexGeneratorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itinerari.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates' / 'html',
        ],
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
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates' / 'latex_generator']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'itinerari.jinja2.environment',
        },
    },
]

WSGI_APPLICATION = 'itinerari.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'itinerari',
        'USER': 'itinerariuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_TZ = True




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GDAL_LIBRARY_PATH = r'C:\Users\Lorenzo\miniconda3\Lib\site-packages\osgeo\gdal'

from latex_generator.settings import *

TEMPLATE_CONTEXT_PROCESSORS = "django.template.context_processors.request"

#######################
# Static configurations
# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = 'static/'

# The absolute path to the directory where collectstatic will collect static files for deployment
STATIC_ROOT = BASE_DIR / "static"

# The additional locations the staticfiles app will traverse
import map
STATICFILES_DIRS = (
    MAIN_APP_DIR / 'static',
    ("map", Path(map.__file__).parent / "static")
)
#######################


SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
    "geojsoncss": "map.serializers.geojsoncss",
 }

LEAFLET_CONFIG = {
    'PLUGINS': {
        'geojsoncss': {
            'js': 'map/js/geojsoncss/geojsoncss.js',
            'auto-include': True,
        }
    }
}

GOOGLE_FONTS = ["Kiwi Maru"]
