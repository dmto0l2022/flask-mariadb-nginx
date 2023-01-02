import dash
from dash import html
import dash_bootstrap_components as dbc
import flask
from flask import session

server = flask.Flask(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],server=server, requests_pathname_prefix='/session_app/')

#session_div =html.Div(html.H1(children="Hello Session!",id='session id div'))

app.layout = html.Div([
            html.H1(children="Hello world!",className="hello",
    style={'color':'#00361c','text-align':'center'
          })
      ])

#app.layout = dbc.Container(
#    dbc.Alert("Hello Bootstrap!", color="success"),
#    session_div,
#    className="p-5",
#)
