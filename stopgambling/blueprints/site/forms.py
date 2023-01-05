from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, StringField, FileField, RadioField, validators

class SelfExclusionForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])

    cnp = IntegerField('Cnp', [validators.Length(min=13,max=13)])

    number_phone = StringField('Number Phone', [validators.Length(min=10,max=10),
                                                validators.DataRequired()
                                                ])

    email_address = StringField('Email Address', [validators.Length(min=6, max=60), 
                                                validators.DataRequired()
                                                ])

    selfie_kyc = FileField('', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

    selected_casinos = RadioField('Select Casinos', 
                                choices=
                                [('Las Vegas','Las Vegas'),
                                ('Don Cash','Don Cash'), 
                                ('All Casinos','All Casinos')
                                ])

    period = RadioField('Select Ban Period', 
                                choices=
                                [('6 Months','6 Months'),
                                ('1 Year','1 Year'), 
                                ('Permanently','Permanently')
                                ])



class RegisterCasinoForm(FlaskForm):
    name = StringField('Casino Name', [validators.Length(min=2, max=25)])
    email = StringField('Email', [validators.Length(min=4, max=25)])
