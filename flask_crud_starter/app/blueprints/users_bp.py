from flask import Blueprint, render_template
from app.models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def index():
    users = User.get_users()
    return render_template('users_simple.html', users=users)
