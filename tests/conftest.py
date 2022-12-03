import pytest
from wsgi import app

@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    with flask_app.test_client() as testing_client:
        yield testing_client

    


