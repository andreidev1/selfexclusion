from stopgambling.models.models import Casino
import datetime
from db import db

def test_new_casino(init_database):
    registered_casino = 'Las Vegas'
    casino = Casino(name=registered_casino, timestamp=str(datetime.datetime.utcnow))


    assert casino.name == 'Las Vegas'
    assert casino.timestamp == str(datetime.datetime.utcnow)

    db.session.add(casino)
    db.session.commit()