import os
import datetime

import jwt
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app
from werkzeug.utils import secure_filename

from db import db
from .forms import SelfExclusionForm, RegisterCasinoForm
from stopgambling.models.models import User, Casino
from stopgambling.globals.functions.utils import encrypt_image_name
from stopgambling.globals.classes.face_recognition import FaceRecognition



site = Blueprint('site', 
                __name__, 
                template_folder='templates/site', 
                static_folder='static',
                static_url_path='/site/static'
                )



@site.route('/', methods=['GET','POST'])
def index():

    form = SelfExclusionForm()
    if request.method == 'POST':
        file = request.files['selfie_kyc']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
        if file:

            # Set path for face recognition feature
            main_path = os.path.join(os.path.dirname(__file__)).replace('\\blueprints\\site', '')
            cascade_path = main_path + '\\globals' + '\\classes' + '\\cascades' + 'haarcascade_frontalface_default.xml' 
            
            # Getting filename and encrypting it for avoiding duplication
            filename = secure_filename(file.filename)
            filename = encrypt_image_name(filename)

            face = FaceRecognition(filename, cascade_path)
            
            face.read_image()

            if face.detect_face():

                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

                new_user = User(

                                name=request.form['name'],
                                cnp=request.form['cnp'],
                                number_phone=request.form['number_phone'],
                                email_address=request.form['email_address'],
                                selfie_kyc=filename,
                                selected_casinos=request.form['selected_casinos'],
                                timestamp = str(datetime.datetime.utcnow()),
                                period=request.form['period']

                                )

                db.session.add(new_user)
                db.session.commit()

                flash('Success ! You were registered in our database')
            
            else:

                flash('Could not recognize face of identity card')
        
    return render_template('index.html', form=form)




@site.route('/register_casino', methods=['GET', 'POST'])
def register():
    form = RegisterCasinoForm()
    
    if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            timestamp = str(datetime.datetime.utcnow())

            payload = dict(name=name, email=email, timestamp=timestamp)
            auth_key = jwt.encode({'data' : payload}, current_app.config['SECRET_KEY'], algorithm='HS256')

       
            new_casino = Casino(name=name, email=email, timestamp=timestamp, auth_key=auth_key)

            db.session.add(new_casino)
            db.session.commit()
        
            flash('Thank you for registration ! You will receive shortly an e-mail with more details.')
            return redirect(url_for('site.register'), 201)
    
    return render_template('casino.html', form=form), 200
