## https://testdriven.io/blog/flask-sessions/
from flask import Blueprint, render_template
from flask_restful import Api, Resource, url_for

session_bp = Blueprint('session_bp', __name__)

@session_bp.route('/session', methods=['GET', 'POST'])
def sessionroot():
    return 'session root'
