import flask

app = flask.FLask(__name__)

with app.test_request_context('/'):

    assert flask.request.path == '/'
    