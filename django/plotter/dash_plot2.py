#import libraries
from os import name
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from .models import LimitOwnerships
import pymysql
import pandas as pd
from django.db import connection

import numpy as np

#def dash_plotly_plot2():
"""
Output: Figure object
"""

query = str(LimitOwnerships.objects.all().query)
df = pd.read_sql_query(query, connection)

#print(df)

#Create graph object Figure object with data
fig3 = go.Figure(go.Scatter(x=df['user_id'], y=df['limit_id']))
   
#    return fig


#Create DjangoDash application
app = DjangoDash(name='DashPlot2', add_bootstrap_links=True)

N = 1000
t = np.linspace(0, 10, 100)
y = np.sin(t)

fig2 = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

#fig3 = dash_plotly_plot2()

#Configure app layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig3,
        style={'width': '50vw', 'height': '50vh'}
    )
],style={'width': '90vh', 'height': '90vh'})

