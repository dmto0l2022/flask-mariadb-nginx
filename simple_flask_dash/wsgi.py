from werkzeug.middleware.dispatcher import DispatcherMiddleware

import flask_app as fs

from app1 import app as app1
from app2 import app as app2

application = DispatcherMiddleware(fs.flask_app, {
    '/app1': app1.server,
    '/app2': app2.server,
})  
