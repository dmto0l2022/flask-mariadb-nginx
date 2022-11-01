import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

def plotly_plot():
    """
    This function plots plotly plot
    """
    import plotly.express as px

    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
   
    #Update layout for graph object Figure
    fig.update_layout(title_text = 'Life expectancy in Canada',
                      xaxis_title = 'year',
                      yaxis_title = 'lifeexp')
    
    #Turn graph object into local plotly graph
    plotly_plot_obj = plot({'data': fig}, output_type='div')

    return plotly_plot_obj