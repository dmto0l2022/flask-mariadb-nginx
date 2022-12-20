from flask import Blueprint, render_template
from app.models.models import User

bp = Blueprint('users', __name__)


@bp.route('/')
def index():
    users = User.get_users()
    return render_template('users_simple.html', users=users)
