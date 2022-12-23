from app import init_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app.dashapps.interactive_table import app as app1

app = init_app()

application = DispatcherMiddleware(app, {
    '/wsgi_app1': app1.server,
})  
