import flask
from flask import Flask, flash, render_template, session
import dash
from dash import html
from dash import dcc

server = flask.Flask(__name__)

dash_app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dashboard/'
)

dash_app.layout = html.Div(style={children=[
    html.H1(
        children='Hello Dash',),
   html.H1(
        id='store_client_id'
        children='Session ID Here'),
])

## that session is then available inside callbacks.

dash_app.callback(
   [Output('store_client_id', 'data')],
   [Input('div3', 'children')])
   def update_user(children):
     try:
         s = session.get('sessionoid', None)
         return s
     except:
         return -10
