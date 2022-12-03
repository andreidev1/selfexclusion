from flask import current_app as app

from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, marshal_with, fields
from models.models import User


api_v1 = Blueprint('api', __name__, subdomain='api')

api = Api(
    api_v1,
    version="1.0",
    title="Todo API",
    description="A simple TODO API",
)


userFields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'password' : fields.String
}


class Users(Resource):
    @marshal_with(userFields)

    def get(self):

        users = User.query.all()

        return users 


api.add_resource(Users, '/users')

'''
    def post(self):
        data = request.json

        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)

        db.session.add(new_user)
        db.session.commit()

        
        return jsonify({'message' : 'New user created!'})


    def put(self):

        data = request.json

        
        promote_user = User.query.filter_by(public_id=data['public_id']).first()

        
        promote_user.admin = True

        
        db.session.commit()

        return {'message' : 'User : ' + promote_user.name + ' promoted'}, 200
        

class GetOneUser(Resource):

    @marshal_with(userFields)

    def get(self, id):

        user = User.query.filter_by(id=id).first()

        return user


class LoginUser(Resource):

    @marshal_with(tokenField)
    def post(self):

        auth = request.authorization

        user = User.query.filter_by(name=auth.username).first()

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            decoded_token = token.decode('UTF-8')
            
            

        return {'token' : decoded_token}
'''




