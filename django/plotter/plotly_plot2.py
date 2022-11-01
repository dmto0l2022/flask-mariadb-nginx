import pandas as pd
import pymysql.cursors
from .models import LimitOwnerships
from plotly.offline import plot
import plotly.graph_objs as go

from django.db import connection



def plotly_plot2():
    """
    This function plots plotly plot
    """
    
    query = str(LimitOwnerships.objects.all().query)
    df = pd.read_sql_query(query, connection)
    
    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=df['user_id'], y=df['limit_id'],
                    mode='markers',
                    name='markers'))


    #Update layout for graph object Figure
    fig.update_layout(title_text = 'Plotly_Plot1',
                      xaxis_title = 'X_Axis',
                      yaxis_title = 'Y_Axis')
    
    #Turn graph object into local plotly graph
    plotly_plot_obj = plot({'data': fig}, output_type='div')

    return plotly_plot_obj