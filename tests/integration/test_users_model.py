
from models.models import User
from models.models import Casino
import datetime
from book_app.globals.utils import verify_cnp, verify_phone, verify_email, hash_image_name





casinos = ['Las Vegas', 'Don Cash', 'Mozzart']    
casino_obj = Casino(name=casinos, timestamp=datetime.datetime.utcnow)

def test_blacklist_user():
    
    user = User(
                name='Andrew', 
                cnp=verify_cnp('1234567890123'), 
                number_phone=verify_phone('0785454541'),
                email_address=verify_email('myusertest@gmail.com'),
                selfie_kyc=hash_image_name('kyc_image.png'),
                verified=False,
                selected_casinos=['Las Vegas', 'Don Cash', 'Mozzart'],
                timestamp=datetime.datetime.utcnow,
                casino = casino_obj
                )



    assert user.name == 'Andrew'
    assert user.cnp == '1234567890123'
    assert user.number_phone == '0785454541'
    assert user.email_address == 'myusertest@gmail.com'
    assert user.selfie_kyc == hash_image_name('kyc_image.png')
    assert user.verified == False
    assert user.selected_casinos == ['Las Vegas', 'Don Cash', 'Mozzart']
    assert user.timestamp == datetime.datetime.utcnow
    assert user.casino == casino_obj






