import json
import datetime
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from app.booking.models import User, UserLogin
from app.db import set_user, get_user_for_login, get_user

class SignupApi(Resource):
    def post(self):
        post_data = request.get_json()
        data_dict = json.loads(json.dumps(post_data))

        user = User(**data_dict)
        user.hash_password()
        
        print('\nUser: ', user.name)
        
        e = set_user(user)

        print('Error', e)

        if e == 1062:
            return {'error':'email already exits'}, 200
        else:
            return {'email': user.email, 'msg': 'was created correctly'}, 200

class LoginApi(Resource):
    def post(self):

        print('='*32)
        print('\n\n entra al post \n\n')
        print('='*32)
        body = request.get_json()
        user_dict  = get_user(body.get('email'))[0]
        
        user = User(**user_dict)
        print('='*32)
        print(f'\n\n usuario: {user.name}\n\n')
        print('='*32)
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        print('='*32)
        print(f'\n\n usuario: {user.phone_number}\n\n')
        print('='*32)

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)

        return {'token': access_token}, 200
    