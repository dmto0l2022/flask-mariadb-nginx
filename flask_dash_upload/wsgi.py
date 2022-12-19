from app import create_app

from werkzeug.wsgi import DispatcherMiddleware

from app.dashapps.app1 import app as app1

app = create_app()

application = DispatcherMiddleware(app, {
    '/app1': app1.server,
})  

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8002')
