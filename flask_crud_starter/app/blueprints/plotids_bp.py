from flask import Blueprint, render_template
##from flask import current_app
from app.models import Plots
from app.forms import EnterNewPlotForm
from datetime import datetime
import json

plotids_bp = Blueprint('plotids_bp', __name__)

@plotids_bp.route('/plots/new/')
def CreateNewPlot():
    name = 'new plot'
    plotid = 'P123455662357989092370'
    plotids = Plots.create(plotid,name)
    y =  {
        "plotid": plotid,
        "name": name
        }
    r = json.dumps(y)
    return r

@plotids_bp.route('/plots/show/')
def showplots():
    allplots = Plots.get_plots()
    return allplots


@plotids_bp.route("/plots/enter", methods=["GET", "POST"])
def EnterNewPlotFunc():
    """Standard 'plot' form."""
    form = EnterNewPlotForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "newplot.html",
        form=form,
        template="form-template"
    )

@plotids_bp.route("/plots/success", methods=["GET", "POST"])
def success():
   return "success"
