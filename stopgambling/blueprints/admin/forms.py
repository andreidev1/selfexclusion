
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class AdminLoginForm(FlaskForm):
    username = StringField('Admin Username', [validators.Length(min=2, max=25)])
    password = PasswordField('Password', [validators.Length(min=4, max=25)])

