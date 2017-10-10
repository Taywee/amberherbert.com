from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

with open('/etc/amberherbert/secret.key', 'r') as file:
    SECRET_KEY = file.read().strip()

try:
    from .local import *
except ImportError:
    pass
