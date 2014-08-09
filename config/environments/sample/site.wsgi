import os
import sys

sys.path.append('/sample/path')
sys.path.append('/sample/path/env/lib/python2.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
