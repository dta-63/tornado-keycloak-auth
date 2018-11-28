import json
import os
from handlers.base import MainHandler
from tornado import web, ioloop

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "open_id_certs_url": "https://KEYCLOAK_SERVER/auth/realms/YOUR_REALM/protocol/openid-connect/certs"
}


def make_app():
    return web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()