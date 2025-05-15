from pathlib import Path
from dotenv import dotenv_values
import os

config = dotenv_values("backend/secret.env")
mysecret = config.get("MY_SECRET")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-27gc#f7c!nw^pw=_&0tnv7^=p$&53^u1i#mp7q+i_4cxu92sky'

MY_SECRET = f'{mysecret}'

ACCESS_TOKEN_EXPIRE = 5

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'bytebooks-backend.fly.dev',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'livros',
    'clientes',
    'carrinho',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

AUTH_USER_MODEL = 'clientes.Cliente'

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

MEDIA_URL  = "/media/"
#MEDIA_ROOT = "/data/media"     # persistente

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    #'https://bytebooks-kappa.vercel.app',
    'http://localhost:8080'
]

#CSRF_TRUSTED_ORIGINS    = ["https://bytebooks-backend.fly.dev"]
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE   = False #debug
CSRF_COOKIE_SECURE      = False #debg
SECURE_SSL_REDIRECT     = False #debug

'''CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'x-requested-with',
]'''

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
  "Authorization",
  "X-CSRFToken",
]

CORS_ALLOW_CREDENTIALS = True
