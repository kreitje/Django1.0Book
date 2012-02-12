import os
import sys

path = '/Users/kreitje/Development/Python'
if path not in sys.path:
    sys.path.append(path)

sys.path.append('/Users/kreitje/Development/Python/jeff')

os.environ['DJANGO_SETTINGS_MODULE'] = 'jeff.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
