from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import flask_app as fa

from app1 import app as app1
from app2 import app as app2

application = DispatcherMiddleware(fa.flask_app, {
    '/app1': app1.server,
    '/app2': app2.server,
})

if __name__ == '__main__':
    run_simple('0.0.0.0', 8002, application) 
   
  
