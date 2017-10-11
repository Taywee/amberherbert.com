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
