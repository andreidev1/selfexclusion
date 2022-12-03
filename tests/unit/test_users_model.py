
from models.models import User
from models.models import Casino
import datetime
import hashlib




# Responsible with verifying a real CNP
def verify_cnp(cnp: str):
    if len(cnp) == 0 or len(cnp) < 13:
        return 'Invalid CNP'
    else:
        return cnp

# Responsible with verifying a real number phone   
def verify_phone(number_phone: str):
    if len(number_phone) == 0 or len(number_phone) < 10:
        return 'Invalid Number Phone'   
    else:
        return number_phone

# Responsible with verifying a real e-mail address
def verify_email(email: str):
    ALLOWED_PROVIDERS = ['gmail.com', 'yahoo.com', 'yandex.com']

    for provider in ALLOWED_PROVIDERS:
        if '@' and provider in email:
            return email
        else:
            return False

# Responsible with hashing image name for avoiding duplication
def hash_image_name(image_name: str):
    ALLOWED_EXTENSIONS = ['.jpg', '.png']

    for extension in ALLOWED_EXTENSIONS:
        if extension in image_name:
            image_name = hashlib.sha256(image_name.encode('utf-8')).hexdigest() + extension

    return image_name

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






