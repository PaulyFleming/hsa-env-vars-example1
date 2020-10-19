import pytest
import flask

app = flask.Flask(__name__)

class TestClass:
    def test_basic_test1(self):
        x = 5
        y = 10
        assert x < y
    