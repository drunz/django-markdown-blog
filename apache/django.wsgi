import os
import sys

path = '/var/websites'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append(path+'/landing')

os.environ['DJANGO_SETTINGS_MODULE'] = 'landing.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
