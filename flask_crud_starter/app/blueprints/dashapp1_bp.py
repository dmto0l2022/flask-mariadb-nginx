from flask import Blueprint, render_template, redirect

dashapp1_bp = Blueprint('dashapp1_bp', __name__)

@dashapp1_bp.route('/dashapp1')
def dashapp1():
    return redirect('/wsgi_app1', code=302)

@dashapp1_bp.route('/dashapp2')
def dashapp1():
    return redirect('/wsgi_app2', code=302)
