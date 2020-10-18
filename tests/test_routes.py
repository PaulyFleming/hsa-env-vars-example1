from flask import flask

def test_base_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'
    
    response = client.get(url)
    assert response.get_data() == b'Hello world. To make requests go to /requests'
    assert response.status_code == 200