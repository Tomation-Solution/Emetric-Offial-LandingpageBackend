"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from urllib.parse import urlparse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-15)r-xg0iak5jwd=8obw49y^6__$6ko4a3&6vk0_^3p14xrw68'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'blog',
    'account',

        "cloudinary_storage",
    "cloudinary",

        'rest_framework',
     'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if os.environ.get('databaseUser',None):
    #here we using the local postgesql in django 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['databaseName'], 
            'USER': os.environ['databaseUser'], 
            'PASSWORD': os.environ['databasePassword'],
            'HOST': os.environ['databaseHost'], 
            'PORT': os.environ['databasePort'],
        }
    }
else:#this means we getting the credtials from heroku
    db_info = urlparse(os.environ.get('DATABASE_URL',None))
    DATABASES = {
    "default": {
    'ENGINE': 'django.db.backends.postgresql',
    "NAME": db_info.path[1:],
    "USER": db_info.username,
    "PASSWORD": db_info.password,
    "HOST": db_info.hostname,
    "PORT": db_info.port,
    "OPTIONS": {"sslmode": "require"},
    "CONN_MAX_AGE": 60,
    }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
'https://www.emetricsuite.com',
'https://emetric-landing-page.herokuapp.com',
'http://emetric-landing-page.herokuapp.com',
'http://localhost:3000'
]

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]

REST_FRAMEWORK = {
    #here am just telling django rest to use this function for my error response 
    'EXCEPTION_HANDLER': 'utils.custom_exception_response.custom_exception_handler',
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
         'rest_framework.authentication.TokenAuthentication'
    ],
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
}

AUTH_USER_MODEL = 'account.User'




# cloudinary settings

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_URL='cloudinary://913891166949297:WmepNxE7KglCurD10dPECBlecKQ@haqszgzma'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['API_KEY'],
    'API_SECRET':os.environ['API_SECRET']
}