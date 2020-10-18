import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = request.args['request']
    try:
        return "Your request is: " + response
    except KeyError:
        return f'Invalid request'
        
