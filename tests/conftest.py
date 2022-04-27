import pytest
from app import app as flask_tests

@pytest.fixture()
def app():
    yield flask_tests

@pytest.fixture
def client(app):
    return app.test_client()
