## https://testdriven.io/blog/flask-sessions/
from flask import Blueprint, render_template, Flask, render_template_string, request, session, redirect, url_for
from flask_restful import Api, Resource, url_for

session_bp = Blueprint('session_bp', __name__)

def createsessionid():
    sessionidnow = datetime.datetime.utcnow().strftime("S%Y%m%d%H%M%S%f")
    return sessionidnow


@session_bp.route('/session', methods=['GET', 'POST'])
def sessionroot():
    return 'session root'


@session_bp.route('/session/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to the session object
        session['email'] = request.form['email_address']
        session['sessionid'] = createsessionid()
        return redirect(url_for('get_email'))

    return """
        <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
        """


@session_bp.route('/session/get_email')
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
            <h1>Session ID : {{ session['sessionid'] }}</h1>
        """)


@session_bp.route('/session/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    session.pop('sessionid', default=None)
    return '<h1>Session deleted!</h1>'
