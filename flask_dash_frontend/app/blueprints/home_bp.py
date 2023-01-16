from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/app/', methods=['GET', 'POST'])
def rootofserver():
    return 'root'

@home_bp.route('/app/home')
def home():
    return render_template('home.html')
