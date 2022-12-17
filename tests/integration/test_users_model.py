
from stopgambling.models.models import User, Casino
import datetime
from stopgambling.globals.functions.utils import verify_cnp, verify_phone, verify_email, hash_image_name
from db import db






def test_blacklist_user(app_ctx):
    #casinos = ['Las Vegas', 'Don Cash', 'Mozzart']
    #edit below (find a way to add list to that field)
    casinos = 'Las Vegas'    
    casino_obj = Casino(name=casinos, timestamp=str(datetime.datetime.utcnow))
    user = User(
                name='Andrew', 
                cnp=verify_cnp('1234567890123'), 
                number_phone=verify_phone('0785454541'),
                email_address=verify_email('myusertest@gmail.com'),
                selfie_kyc=hash_image_name('kyc_image.png'),
                verified=False,
                selected_casinos='Las Vegas',
                timestamp=str(datetime.datetime.utcnow),
                casino = casino_obj
                )
    
    assert user.name == 'Andrew'
    assert user.cnp == '1234567890123'
    assert user.number_phone == '0785454541'
    assert user.email_address == 'myusertest@gmail.com'
    assert user.selfie_kyc == hash_image_name('kyc_image.png')
    assert user.verified == False
    assert user.selected_casinos == 'Las Vegas'
    assert user.timestamp == str(datetime.datetime.utcnow)
    assert user.casino == casino_obj
    


    db.session.add(user)
    db.session.commit()






