
from stopgambling.models.models import User
import datetime
from stopgambling.globals.functions.utils import verify_cnp, verify_phone, verify_email, encrypt_image_name
from db import db


def test_blacklist_user(init_database):
  

    user = User(
                name='Andrew', 
                cnp=verify_cnp('1234567890123'), 
                number_phone=verify_phone('0785454541'),
                email_address=verify_email('myusertest@gmail.com'),
                selfie_kyc=encrypt_image_name('kyc_image.png'),
                verified=False,
                selected_casinos='Las Vegas',
                timestamp=str(datetime.datetime.utcnow),
                period='Permanently'
                )

    assert user.name == 'Andrew'
    assert user.cnp == '1234567890123'
    assert user.number_phone == '0785454541'
    assert user.email_address == 'myusertest@gmail.com'
    assert user.selfie_kyc == user.selfie_kyc
    assert user.verified == False
    assert user.selected_casinos == 'Las Vegas'
    assert user.timestamp == str(datetime.datetime.utcnow)
    assert user.period == 'Permanently'
    


    db.session.add(user)
    db.session.commit()






