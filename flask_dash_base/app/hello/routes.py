import os
from flask import Flask, flash, request, redirect, url_for, render_template

from flask import Blueprint

hello_page_bp = Blueprint('hello_page_bp', __name__)

@hello_page_bp.route('/')
def index():
     return "Hello this is the landing site"

@hello_page_bp.route('/app/')
def hello():
    return "Hello, World!"

@hello_page_bp.route('/app/welcome/')
def welcome():
    return render_template('welcome.html')
