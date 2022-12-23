from app import init_app

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app.dashapps.interactive_table import app as app1
from app.dashapps.basic_table import app as app2

application = init_app()
