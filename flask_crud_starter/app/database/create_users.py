"""
Insert dummy data into database
"""
from app import init_app
from app.models.models import User

def insert_dummy_data():
    flask_app = init_app()
    with flask_app.app_context():
        User.create('adam123', 'Adam', 'adam@gmail.com')

