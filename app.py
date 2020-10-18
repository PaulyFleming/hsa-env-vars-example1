import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = request.args['request']
    try:
        if response:
            return "Your request is: " + response
        else:
            return "Please enter a request using using ?response=foo"
    except KeyError:
        return f'Invalid request'
        
