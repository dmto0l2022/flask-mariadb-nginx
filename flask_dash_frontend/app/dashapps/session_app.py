import dash
from dash import html
import dash_bootstrap_components as dbc
import flask
from flask import session

server = flask.Flask(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],server=server, requests_pathname_prefix='/session_app/')

session_div =html.div(id='session id div', children="S123455667")

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    session_div,
    className="p-5",
)
