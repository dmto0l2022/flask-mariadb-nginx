import dash
import dash_bootstrap_components as dbc
import flask

server = flask.Flask(__name__)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],server=server, requests_pathname_prefix='/session_app/')

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)
