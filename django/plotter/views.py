#import libraries
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connections
from django.contrib import messages
from django.urls import reverse
import pandas as pd
import pymysql.cursors
from plotly.offline import plot
import plotly.graph_objs as go
from .plotly_plot2 import *

def index(request):
    ...
    #Plotly visualizations
    target_plot = plotly_plot2()
    ...
    #Return context to home page view
    context = {'target_plot': target_plot,}
        
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'plotly.html',
        context= context)


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the plotter index.")
