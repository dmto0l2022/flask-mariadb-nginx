import dash
import dash_html_components as HTML

app = dash.Dash(
    __name__,
    requests_pathname_prefix='/app2/'
)

app.layout = html.Div("Dash app 2") 
