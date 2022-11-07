from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/user')
def index():
    user = {'username': 'Andy'}
    return render_template('basic.html', title='Basic', user=user)
