from werkzeug.security import check_password_hash, generate_password_hash
from dataclasses import dataclass

@dataclass
class Admin:
    username: str
    password: str

    def hash(self):

        hashed_password = generate_password_hash(self.password, method='sha256')

        return hashed_password

def test_login_admin():
    admin = Admin('Admin', 'password')


    assert check_password_hash(admin.hash(), admin.password)
    assert admin.username == 'Admin'
    assert admin.password == 'password'
