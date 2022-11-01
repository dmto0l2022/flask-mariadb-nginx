# mysite/routing.py
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    # (your routes here)
    "http": get_asgi_application(),
})

