from models.models import Casino
import datetime

def test_new_casino():
    casinos = ['Las Vegas', 'Don Cash', 'Mozzart']
    casino = Casino(name=casinos, timestamp=datetime.datetime.utcnow)

    assert casino.name == ['Las Vegas', 'Don Cash', 'Mozzart']
    assert casino.timestamp == datetime.datetime.utcnow