from db import db
import datetime

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cnp = db.Column(db.String(50))
    number_phone = db.Column(db.String(12))
    email_address = db.Column(db.String(60))
    selfie_kyc = db.Column(db.String(80))
    verified = db.Column(db.Boolean, default=False)
    selected_casinos = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('casino.id'))



class Casino(db.Model):

    __tablename__ = 'casino'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    users = db.relationship('User', backref='casino')    