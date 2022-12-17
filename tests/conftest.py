import datetime

import pytest

from wsgi import app
from stopgambling.models.models import User
from db import db

@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    with flask_app.test_client() as testing_client:
        
        yield testing_client


@pytest.fixture(scope='module')
def app_ctx(app=app):
    with app.app_context():
        db.create_all()
        yield

        db.drop_all()

       


@pytest.fixture(scope='module')
def new_user():
    pass

@pytest.fixture(scope='module')
def new_casino():
    pass