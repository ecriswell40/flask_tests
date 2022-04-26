import pytest
from app import app as vtm_tank1

@pytest.fixture()
def app():
    yield vtm_tank1

@pytest.fixture
def client(app):
    return app.test_client()
