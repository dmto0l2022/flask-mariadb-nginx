from myapp import app, db

# Set up models
with app.app_context():
    db.create_all()
