import flask
from flask import request
from environs import Env
import os

app = flask.Flask(__name__)

env = Env()
env.read_env()
development = os.environ.get('DEVELOPMENT')

# get PORT from os, or use 5000 if not set
port = int(os.environ.get('PORT', 5000))

@app.route('/', methods=['GET'])
def home():
    print(f"Development environment = {development}", flush=True)

    response = request.args['request']
    try:
        return "Your request is: " + response
        
    except KeyError:
        return f'Invalid request'
        

print(f"App booted succesfully on Port: {port}", flush=True )
