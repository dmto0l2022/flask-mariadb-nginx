import dash
from dash import html
import dash_bootstrap_components as dbc
import flask
from flask import session, jsonify
import json

server = flask.Flask(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],server=server, requests_pathname_prefix='/session_app/')

app.layout = html.Div([
            html.H1(children="Hello world!",className="hello",id="div3",
    style={'color':'#00361c','text-align':'center'
          }),
            html.H1(children="session id" ,id="div2",
    style={'color':'#00361c','text-align':'center'
          })
      ])

@app.callback(
	Output('div2', 'children'),
	[Input('div3', 'children')])
def update_id(children):
	return 'id: {}'.format(session.get('sessionid', None))


#app.layout = dbc.Container(
#    dbc.Alert("Hello Bootstrap!", color="success"),
#    session_div,
#    className="p-5",
#)
