#from flask import Flask, request
#from flask_restful import Resource, Api

#app = Flask(__name__)
#api = Api(app)
##app.config['APPLICATION_ROOT'] = '/flask1'
#api = Api(app, prefix='/flask1')

#class Greeting (Resource):
#    def get(self):
#        return 'Hello World!'

#api.add_resource(Greeting, '/') # Route_1

#if __name__ == '__main__':
#    app.run('0.0.0.0','5000')

from flask import Flask
app = Flask(__name__)
#app.config['APPLICATION_ROOT'] = '/flask1'
##CORS(app) #Prevents CORS errors 
@app.route(‘/’)
def index():
    return “Hello, World!”

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)
