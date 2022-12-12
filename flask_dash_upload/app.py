from flask import Flask, flash, request, redirect, url_for
## both following dead ends
##from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
## from flask_uploads import UploadSet, configure_uploads

import os

from werkzeug.utils import secure_filename

#UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def create_app():
    app = Flask(__name__)
    app.config.from_object('myconfig.conf')
    #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    from hello.routes import hello_page_bp
    from upload.routes import upload_page_bp
    app.register_blueprint(hello_page_bp)
    app.register_blueprint(upload_page_bp)
    return app
