from flask import Blueprint, render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators

site = Blueprint('site', 
                __name__, 
                template_folder='templates/site', 
                static_folder='static',
                static_url_path='/site/static'
                )


class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@site.route('/')

def index():
    return render_template('index.html')


@site.route('/submit-data', methods=['GET','POST'])
def submitData():
           
    return 'sall'

