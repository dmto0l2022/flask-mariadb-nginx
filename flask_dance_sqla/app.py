from minimal_app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Set up models
with app.app_context():

    db.create_all()
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    u_all = User.query.all()
    #[<User u'admin'>, <User u'guest'>]
    print(u_all)
    u_admin = User.query.filter_by(username='admin').first()
    #<User u'admin'>
    print(u_admin)

