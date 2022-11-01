#import libraries
from os import name
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd

from dash import Dash, dcc, html, Input, Output
import plotly.express as px


def dash_plotly_plot(mysql_connection, city):
    """
    This function creates dash app for plotting variable stats by city selected
    Input: Mysql connection and city specified
    Output: Figure object
    """
    #Create SQL command string
    df = px.data.tips() # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", 
                 color="smoker", barmode="group")
    return fig


#Create DjangoDash applicaiton
app = DjangoDash('SimpleExample123456')

#Configure app layout
app.layout = html.Div([
    html.H4('Restaurant tips by day of week'),
    dcc.Dropdown(
        id="dropdown",
        options=["Fri", "Sat", "Sun"],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

#Define app input and output callbacks
@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(day):
    df = px.data.tips() # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", 
                 color="smoker", barmode="group")
    return fig