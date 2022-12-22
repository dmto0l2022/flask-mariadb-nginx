from flask import Blueprint, render_template
from . import models

users_bp = Blueprint('plotids_bp', __name__)

@plotid_bp.route('/plotsids/')
def index():
    plotids = Plots.get_plotids()
    return render_template('plotids_simple.html', plotid=plotids)
