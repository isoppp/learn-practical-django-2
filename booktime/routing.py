from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
import main.routing

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(URLRouter(main.routing.websocket_urlpatterns)),
        "http": URLRouter(main.routing.http_urlpatterns + [re_path(r"", AsgiHandler)]),
    }
)
