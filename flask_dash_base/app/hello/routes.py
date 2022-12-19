from flask import Blueprint
hello_page_bp = Blueprint('hello_page_bp', __name__)

@hello_page_bp.route('/')
def index():
     return "Hello this is the landing site"

@app.route('/app/')
def hello():
    return "Hello, World!"

@app.route('/app/welcome/')
def welcome():
    return render_template('welcome.html')
