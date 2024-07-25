"""
WSGI config for catcollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catcollector.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catcollector.settings')
>>>>>>> 9b4e396adaec23043e4f1f29ffbb455999e9633b

application = get_wsgi_application()
