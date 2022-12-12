from flask import Flask, flash, request, redirect, url_for
## both following dead ends
##from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
## from flask_uploads import UploadSet, configure_uploads

import os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    from hello.routes import route_blueprint as rbh
    from upload.routes import route_blueprint as rbu
    app.register_blueprint(rbh)
    app.register_blueprint(rbu)
    return app
