import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon_nao.settings")

application = get_asgi_application()
