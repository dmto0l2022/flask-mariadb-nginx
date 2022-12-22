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

 @staticmethod
    def create(plotid,name):
        """
        Create new plot
        """
        new_plots = Plots(plotid,name)
        Base.session.add(new_plots)
        Base.session.commit()

    @staticmethod
    def get_plots():
        """
        :return: list of user details
        """
        plots = [
            {
                'id': i.id,
                'plotid': i.plotid,
                'name': i.name,
            }
            for i in Plots.query.order_by('id').all()
        ]
        return plots
