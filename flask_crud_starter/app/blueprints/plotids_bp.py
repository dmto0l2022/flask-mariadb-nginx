from flask import Blueprint, render_template
from . import models
from . import db
from datetime import datetime
users_bp = Blueprint('plotids_bp', __name__)

@plotid_bp.route('/plots/new/')
def index():
    name = 'new plot'
    plotid = 'P123455662357989092370'
    plotids = Plots.create(plotid,name)
    return jsonify(
        name=name,
        plotid=plotid
    ) 

@plotid_bp.route('/plots/show/')
def index():
    allplots = Plots.get_plots(plotid,name)
    return allplots

