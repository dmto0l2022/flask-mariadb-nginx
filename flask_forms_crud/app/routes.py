#from flask import render_template
from flask import render_template, flash, redirect, url_for, request

from flask import Flask, render_template_string

##from app import app
from flask import current_app

from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password

from flask_login import current_user

from flask_security.models import fsqla_v3 as fsqla

from . import notes as notes

# Views
@current_app.route("/")
def home():
    return render_template_string('Home is where the heart is !')

@current_app.route("/hello")
@auth_required()
def hello():
    return render_template_string('Hello {{email}} !', email=current_user.email)

@current_app.route('/app/welcome/')
@auth_required()
def welcome():
    return render_template('welcome.html')

@current_app.route("/notes/", methods=["POST", "GET"])
def view_index():
    if request.method == "POST":
        notes.create_note(request.form['text'])
    return render_template("index_form.html", notes=notes.read_notes())


@current_app.route("/notes/edit/<note_id>", methods=["POST", "GET"])
def edit_note(note_id):
    if request.method == "POST":
        notes.update_note(notes.note_id, text=request.form['text'], done=request.form['done'])
    elif request.method == "GET":
        notes.delete_note(note_id)
    return redirect("/notes/", code=302)
