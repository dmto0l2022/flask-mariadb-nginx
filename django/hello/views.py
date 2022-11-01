from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
# Create your views here.
from django.http import HttpResponse

#######
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connections
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
from .plotly_plot import *

#######

#from .dash_plot import *


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    
    #Plotly visualizations
    target_plot = plotly_plot()
    
    #Return context to home page view
    context = {'target_plot': target_plot,}
        
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context= context)
        


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
