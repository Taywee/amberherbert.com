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
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/amberherbert/log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'WARNING',
        'propagate': True,
    }
}
STATIC_ROOT = '/var/lib/www/static'
MEDIA_ROOT = '/var/lib/www/media'
