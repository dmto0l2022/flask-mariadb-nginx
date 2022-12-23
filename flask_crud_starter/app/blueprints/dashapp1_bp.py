from flask import Blueprint, render_template, redirect

home_bp = Blueprint('dashapp1_bp', __name__)

@dashapp1_bp.route('/dashapp1')
def dashapp1():
    return redirect("/dashapp1", code=302)
