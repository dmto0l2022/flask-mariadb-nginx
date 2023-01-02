from app import init_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app.dashapps.interactive_table import app as app1
from app.dashapps.basic_table import app as app2
from app.dashapps.session_app import app as app3

app = init_app()

application = DispatcherMiddleware(app, {
    '/wsgi_app1': app1.server,
    '/wsgi_app2': app2.server,
    '/session_app': app3.server,
})  
