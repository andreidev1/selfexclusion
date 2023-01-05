import datetime

import pytest
from werkzeug.security import generate_password_hash

from wsgi import app
from stopgambling.models.models import Admin
from db import db

@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            # Establish an application context
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Create admin credentials
    admin = Admin(username='admin', password=generate_password_hash('admin', method='sha256'))

    # Commit admin credentials to db
    db.session.add(admin)
    db.session.commit()

    yield

    # Drop all tables from db
    db.drop_all()

       


@pytest.fixture(scope='module')
def new_user():
    pass

@pytest.fixture(scope='module')
def new_casino():
    pass