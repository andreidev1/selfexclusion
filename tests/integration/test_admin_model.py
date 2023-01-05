from stopgambling.models.models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

def test_check_admin_credentials(init_database):
    hashed_password = generate_password_hash('admin')

    new_admin = Admin(username='admin', password=hashed_password)
    
    db.session.add(new_admin)
    db.session.commit()

    assert check_password_hash(new_admin.password, 'admin') == True