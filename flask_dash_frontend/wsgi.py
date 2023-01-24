from app import init_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from werkzeug.wrappers import Request, Response, ResponseStream


from app.dashapps.interactive_table import app as app1
from app.dashapps.basic_table import app as app2
from app.dashapps.session_app import app as app3

from app.dashpages.app import app as app4

app = init_app()

application = DispatcherMiddleware(app, {
    '/wsgi_app1': app1.server,
    '/wsgi_app2': app2.server,
    '/session_app': app3.server,
    '/multipage': app4.server,
})  

class Middleware:

    def __init__(self, wsgi, app):
        self.wsgi = wsgi
        self.app = app

    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        request = Request(environ)
        print('path: %s, url: %s' % (request.path, request.url))
        # just do here everything what you need
        return self.app(environ, start_response)


applicationapp.wsgi_app = Middleware(application.wsgi_app, application)
