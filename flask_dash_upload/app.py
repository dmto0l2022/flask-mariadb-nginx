from flask import Flask
## both following dead ends
##from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
## from flask_uploads import UploadSet, configure_uploads

def create_app():
    app = Flask(__name__)
    from hello.routes import route_blueprint as rbh
    from upload.routes import route_blueprint as rbu
    app.register_blueprint(rbh)
    app.register_blueprint(rbu)
    return app
