import os

from django.core.wsgi import get_wsgi_application

root_path = os.path.abspath(os.path.split(__file__)[0])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sargons.settings")

application = get_wsgi_application()
