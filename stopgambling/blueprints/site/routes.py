import os

from flask import Blueprint, render_template, request, flash

from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import BooleanField, StringField, FileField, RadioField, validators
from werkzeug.utils import secure_filename
from stopgambling.models.models import User, Casino

from flask import current_app
from db import db


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
    selfie_kyc = FileField('', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    selected_casinos = RadioField('Select Casinos', choices=[('value','Las Vegas'),('value_two','Don Cash'), ('value_three','All Casinos')])




@site.route('/', methods=['GET','POST'])
def index():
    form = SelfExclusionForm()
    #if form.validate_on_submit():
    if request.method == 'POST':
        file = request.files['selfie_kyc']
        print(file)
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            new_user = User(
                            name=request.form['name'],
                            cnp = request.form['cnp'],
                            number_phone = request.form['number_phone'],
                            email_address = request.form['email_address'],
                            selfie_kyc = request.form['selfie_kyc'],
                            selected_casinos = request.form['selected_casinos']
            
                            )

            db.session.save(new_user)
            db.session.commit()
        
    return render_template('index.html', form=form)

