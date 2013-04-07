from .base import *

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'cah_django.db',
                'USER': '',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
        }
}

STATIC_URL = 'http://philipjohnjames.com/applesanon/static/'

INSTALLED_APPS += (
    'gunicorn',
)