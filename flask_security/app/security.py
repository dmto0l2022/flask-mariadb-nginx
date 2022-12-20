##https://stackoverflow.com/questions/14793098/how-to-use-flask-security-register-view
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_REGISTER_URL'] = '/app/register'
app.config['SECURITY_LOGIN_URL'] = '/app/login'
app.config['SECURITY_LOGOUT_URL'] = '/app/logout'
app.config['SECURITY_RESET_URL'] = '/app/reset'
app.config['SECURITY_CHANGE_URL'] = '/app/change'
app.config['SECURITY_CONFIRM_URL'] = '/app/confirm'
app.config['SECURITY_POST_LOGIN_VIEW'] = '/app/welcome'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/app/login'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/app/welcome'
app.config['SECURITY_POST_CONFIRM_VIEW'] = '/app/welcome'
app.config['SECURITY_POST_RESET_VIEW'] = '/app/welcome'
app.config['SECURITY_POST_CHANGE_VIEW'] = '/app/welcome'
app.config['SECURITY_UNAUTHORIZED_VIEW'] = '/app/register'
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_TRACKABLE='] = True
app.config['SECURITY_CHANGEABLE'] = True

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
app.security = Security(app, user_datastore)
