import flask

app = flask.FLask(__name__)

def test_base_route('/'):

    assert flask.request.path == '/''
    