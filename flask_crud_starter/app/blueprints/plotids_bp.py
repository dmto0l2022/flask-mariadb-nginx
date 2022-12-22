from flask import Blueprint, render_template
##from flask import current_app
from app.models import Plots
from datetime import datetime
import json

plotids_bp = Blueprint('plotids_bp', __name__)

@plotids_bp.route('/plots/new/')
def newplots():
    name = 'new plot'
    plotid = 'P123455662357989092370'
    plotids = Plots.create(plotid,name)
    return json.dumps(name=name,plotid=plotid) 

@plotids_bp.route('/plots/show/')
def showplots():
    allplots = Plots.get_plots()
    return json.dumps(allplots.serialize())
