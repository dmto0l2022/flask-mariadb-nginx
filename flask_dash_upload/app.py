from flask import Flask

def create_app():
    app = Flask(__name__)
    from hello.routes import route_blueprint
    app.register_blueprint(route_blueprint)
    return app
