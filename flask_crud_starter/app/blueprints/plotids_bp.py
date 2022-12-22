from flask import Blueprint, render_template
##from flask import current_app
from app.models import Plots
from app.forms import EnterNewPlotForm
from datetime import datetime
import json
import date

def stringdate():
    today = date.today()
    date_list = str(today).split('-')
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string

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


#####

# add a new sock to the database
@app.route('/plot/create', methods=['GET', 'POST'])
def FuncCreatePlot():
    form1 = FormCreatePlot()
    if form1.validate_on_submit():
        name = request.form['name']
        plotid = request.form['plotid']
        Plots.create(plotid,name)
        # create a message to send to the template
        message = f"The data for sock {plotid} has been submitted."
        return render_template('create_plot.html', message=message)
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('create_plot.html', form1=form1)

# select a record to edit or delete
@app.route('/select_record/<letters>')
def select_record(letters):
    # alphabetical lists by sock name, chunked by letters between _ and _
    # .between() evaluates first letter of a string
    a, b = list(letters)
    socks = Sock.query.filter(Sock.name.between(a, b)).order_by(Sock.name).all()
    return render_template('select_record.html', socks=socks)

# edit or delete - come here from form in /select_record
@app.route('/edit_or_delete', methods=['POST'])
def edit_or_delete():
    id = request.form['id']
    choice = request.form['choice']
    sock = Sock.query.filter(Sock.id == id).first()
    # two forms in this template
    form1 = AddRecord()
    form2 = DeleteForm()
    return render_template('edit_or_delete.html', sock=sock, form1=form1, form2=form2, choice=choice)

# result of delete - this function deletes the record
@app.route('/delete_result', methods=['POST'])
def delete_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    sock = Sock.query.filter(Sock.id == id).first()
    if purpose == 'delete':
        db.session.delete(sock)
        db.session.commit()
        message = f"The sock {sock.name} has been deleted from the database."
        return render_template('result.html', message=message)
    else:
        # this calls an error handler
        abort(405)

# result of edit - this function updates the record
@app.route('/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    # call up the record from the database
    sock = Sock.query.filter(Sock.id == id).first()
    # update all values
    sock.name = request.form['name']
    sock.style = request.form['style']
    sock.color = request.form['color']
    sock.quantity = request.form['quantity']
    sock.price = request.form['price']
    # get today's date from function, above all the routes
    sock.updated = stringdate()

    form1 = AddRecord()
    if form1.validate_on_submit():
        # update database record
        db.session.commit()
        # create a message to send to the template
        message = f"The data for sock {sock.name} has been updated."
        return render_template('result.html', message=message)
    else:
        # show validaton errors
        sock.id = id
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_or_delete.html', form1=form1, sock=sock, choice='edit')
