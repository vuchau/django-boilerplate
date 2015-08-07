from .base import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_boilerplate',
        'USER': 'django',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
