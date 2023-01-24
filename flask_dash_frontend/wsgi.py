from app import init_app

from urllib.parse import urlparse, urlunparse

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from werkzeug.wrappers import Request, Response, ResponseStream

from werkzeug.debug import DebuggedApplication

from werkzeug.utils import redirect

from app.dashapps.interactive_table import app as app1
from app.dashapps.basic_table import app as app2
from app.dashapps.session_app import app as app3

from app.dashpages.app import app as app4

app = init_app()

class Middleware:

    def __init__(self, wsgi):
        self.wsgi = wsgi
        
    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        request = Request(environ)
        url_return_parts = urlparse(request.url)
        url_return_parts._replace(path='/app/welcome')
        url_return = urlunparse(url_return_parts)
        print('path: %s, url: %s' % (request.path, request.url))
        # just do here everything what you need
        if 'wsgi' in request.path:
            #url_return = urlparse(request.url)
            #url_return._replace(path='/app/welcome')
            start_response('301 Redirect', [('Location', url_return),])
            return []
        else:
            return self.wsgi(environ, start_response)


app.wsgi_app = Middleware(app.wsgi_app)

application = DispatcherMiddleware(app, {
    '/wsgi_app1': app1.server,
    '/wsgi_app2': app2.server,
    '/session_app': app3.server,
    '/multipage': app4.server,
})  

application = DebuggedApplication(application, True)
