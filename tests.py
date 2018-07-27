import flask_webtest
import pytest

from app import app


class TestViews:
    @classmethod
    def setup_class(cls):
        app.testing = True
        cls.client = flask_webtest.TestApp(app)

    def test_default(self):
        resp = self.client.get('/')
        assert resp.body == b'Hello World!'

    def test_url_name(self):
        resp = self.client.get('/DerbyPy')
        assert resp.body == b'Hello DerbyPy!'

    def test_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.client.get('/error')
        assert 'Deliberate error' in str(excinfo.value)
