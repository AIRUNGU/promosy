from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import reporter.routing
application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(
        URLRouter(
            reporter.routing.websocket_urlpatterns
        )
    ),
})