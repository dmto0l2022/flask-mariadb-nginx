import flask
from flask import Flask, flash, render_template
import dash
import dash_html_components as html
import dash_core_components as dcc
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import pandas as pd


server = flask.Flask(__name__)

@server.route("/")
def welcome():
   return render_template("home.html")

@server.route("/home", methods=["GET","POST"])
def home():
     if request.method=="POST":
          DATE = request.form["date"]
          try:
               return render_template("success.html")
          except ClientError as e:
               return render_template("failure.html")
     else:
          return render_template("home.html")

dash_app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dashboard/'
)

file = 'test_file_{}.dat'.format(DATE)

df = pd.read_csv(file, header = 0)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
dash_app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x':df['col1'], 'y':df['col2'], 'type': 'bar', 'name': 'SF'},
                {'x':df['col1'], 'y':df['col3'], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

@server.route('/dashboard/')
def render_dashboard():
    return flask.redirect('/dash1')
