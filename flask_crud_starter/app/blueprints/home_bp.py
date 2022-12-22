from flask import Blueprint, render_template

users_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html')
