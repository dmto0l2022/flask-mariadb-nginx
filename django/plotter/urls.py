from django.urls import path

from . import views
from django.views.generic.base import TemplateView # new

from plotter import dash_plot2

from . import plotly_plot2

urlpatterns = \
[
    path('dash2/', TemplateView.as_view(template_name='dash2.html'), name='dash2'),
    path('', views.index, name='index'),
]