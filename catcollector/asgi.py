"""
ASGI config for catcollector project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catcollector.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catcollector.settings')
>>>>>>> 9b4e396adaec23043e4f1f29ffbb455999e9633b

application = get_asgi_application()
