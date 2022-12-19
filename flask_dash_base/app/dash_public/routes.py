from dash import Dash
from dash import html
##from werkzeug.wsgi import DispatcherMiddleware
##from werkzeug.middleware.dispatcher import DispatcherMiddleware
#from flask import Blueprint
import flask
from flask import current_app, Blueprint, render_template
dash_public_page_bp = Blueprint('dash_public_page_bp', __name__)

server = flask.Flask(__name__)
#dash_app1 = Dash(__name__, server = server, url_base_pathname='/dash1/')
#dash_app1.layout = html.Div([html.H1('Hi there, I am Dash1')])

@app.route('/app1')
def show_dash():
    return flask.send_file('/app1')

@dash_public_page_bp.route('/dmpublic/embed')
def publiclembed():
     #return "This will be a public dash landing"
     return flask.redirect('/app1')

@dash_public_page_bp.route('/dmpublic/')
def publiclanding():
     #return "This will be a public dash landing"
     return flask.redirect('/app1')

@dash_public_page_bp.route('/dmpublic/first')
def publicdash():
     #return "This will be a public dash app"
     return flask.render_template('dash.html')

#current_app.wsgi_app = DispatcherMiddleware(server, {'/dash1': dash_app1.server})

#current_app = DispatcherMiddleware(server, {
#    '/dash1': dash_app1.server
#})

'''
from dash import Dash
from werkzeug.wsgi import DispatcherMiddleware
import flask
from werkzeug.serving import run_simple
import dash_html_components as html

server = flask.Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/dashboard/')
dash_app2 = Dash(__name__, server = server, url_base_pathname='/reports/')
dash_app1.layout = html.Div([html.H1('Hi there, I am Dash1')])
dash_app2.layout = html.Div([html.H1('Hi there, I am Dash2')])
@server.route('/')
@server.route('/hello')
def hello():
    return 'hello world!'

@server.route('/dashboard/')
def render_dashboard():
    return flask.redirect('/dash1')


@server.route('/reports/')
def render_reports():
    return flask.redirect('/dash2')

app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
    '/dash2': dash_app2.server
})


@app.route('/maps/map.html')
def show_map():
    return flask.send_file('/maps/map.html')

Flask will automatically prepend your server's address (http://127.0.0.1:4995) to the beginning of any route that you define.

Also, in the template for your HTML, I would use url_for to get the URL for the map to avoid changes in your routes requiring changes to your templates.

<iframe src="{{ url_for('show_dash') }}"></iframe>


'''
