"""
Django settings for kutt project.

Generated by 'django-admin startproject' using Django 2.0.4.


For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,"templates")
PRODUCTION_HOST = 'kutt.fossgect.club'
DB_HOST = None
DB_USER = 'root'
DB_PASS = 'root'
URL_HASH_SIZE = 8

EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k+e(-c(o(vl^^t*_siup0_p+s9jk4z4-t+1-+0tg12*kp%55&^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION_MODE = False


CURRRENT_HOST = None

if PRODUCTION_MODE:
    DB_HOST = 'srv-captain--mysql'
    DB_USER = 'root'
    DB_PASS = 'foss_2255'
    CURRRENT_HOST = PRODUCTION_HOST
    ALLOWED_HOSTS = [PRODUCTION_HOST]
else:
    CURRRENT_HOST = '127.0.0.1'
    DB_USER = 'kutt'
    DB_PASS = 'kutt'
    DB_HOST = '127.0.0.1'
    ALLOWED_HOSTS = [CURRRENT_HOST]


ALLOWED_HOSTS = [ '127.0.0.1', '0.0.0.0', 'localhost', 'xenial.xyz' ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_user_agents',
    'social_django',
    'shortify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'kutt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'kutt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    'static',
]


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '332606479611-7tsa26qspvgbuk2cp51m6i4o9iu3o0rq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '3B2kwll5-L6bE0UY_uNmLpqF'

SOCIAL_AUTH_FACEBOOK_KEY = '2118223078454365'
SOCIAL_AUTH_FACEBOOK_SECRET = '4ba79545d294e1c7ac866fdd5b72b7d6'

SOCIAL_AUTH_GITHUB_KEY = '505bb0c675d4e8db67a5'
SOCIAL_AUTH_GITHUB_SECRET = 'ed381761bf131d00cddfb5b87452d39b4efaf2b5'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',

    'social_core.backends.facebook.FacebookOAuth2',

    'social_core.backends.github.GithubOAuth2',



    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'