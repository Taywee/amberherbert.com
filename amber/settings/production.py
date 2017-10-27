from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['amberherbert.com']

with open('/etc/amberherbert/secret.key', 'r') as file:
    SECRET_KEY = file.read().strip()

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amberherbert',
        'USER': 'www',
    }
}

LOGGING = {
    'version': 1,
    'handlers': {
        'log': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/amberherbert/log',
        },
        'request': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/amberherbert/request',
        },
        'django': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/amberherbert/django',
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['request'],
            'level': 'WARNING',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['django'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['log'],
        'level': 'WARNING',
        'propagate': True,
    },
}
STATIC_ROOT = '/var/lib/www/static'
MEDIA_ROOT = '/var/lib/www/media'
