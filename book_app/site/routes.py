from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import BooleanField, StringField, FileField, validators
from models.models import User, Casino

site = Blueprint('site', 
                __name__, 
                template_folder='templates/site', 
                static_folder='static',
                static_url_path='/site/static'
                )


class SelfExclusionForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    cnp = StringField('Cnp', [validators.Length(min=13,max=13)])
    number_phone = StringField('Number Phone', [validators.Length(min=13,max=13),
                                                validators.DataRequired()
                                                ])
    email_address = StringField('Email Address', [validators.Length(min=6, max=60), 
                                                validators.DataRequired()
                                                ])
    selfie_kyc = FileField('selfie', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    selected_casinos = StringField('Selected Casinos', [validators.DataRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@site.route('/')

def index():
    form = SelfExclusionForm()
    if form.validate_on_submit():
        pass
    return render_template('index.html', form=form)


@site.route('/submit-data', methods=['GET','POST'])
def submitData():
           
    return 'sall'

