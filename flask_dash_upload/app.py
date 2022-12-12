from flask import Flask
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

def create_app():
    app = Flask(__name__)
    from hello.routes import route_blueprint as rbh
    from upload.routes import route_blueprint as rbu
    app.register_blueprint(rbh)
    app.register_blueprint(rbu)
    return app
