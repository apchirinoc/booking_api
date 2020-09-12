import json
from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.booking.models import User, UserLogin
from app.db import set_user, get_user_for_login, get_user, update_user

class UserResource(Resource):
    """ API UserResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """
    @jwt_required    
    def get(self):
        user = User(1,
                    'Andres',
                    'Santos', 
                    'asdasd@gmail.com',
                    '123*',
                    '+573013787020',
                    'Carrera tal con calle x',
                    'img',
                    1125,
                    1,
                    0,0,
                    '','',True)

        s = jsonify(user.__dict__)

        return s
    
    @jwt_required
    def post(self):
        return {'msg': 'postMethod'}

    @jwt_required  
    def put(self):
        body = request.get_json()
        user_dict_updated = json.loads(json.dumps(body))

        user_updated = User(**user_dict_updated)

        print(user_updated.email)

        result = get_user_for_login(user_updated.email)[0]

        if result['row_count'] == 1:
            e = update_user(user_updated)
            return {'msg': f'user {user_updated.email} updated'}
        else:
            return {'error': 'email does not exist'}

    @jwt_required  
    def patch(self):
        body = request.get_json()
        user_for_log_dict_updated = json.loads(json.dumps(body))
        user_for_log_updated = UserLogin(**user_for_log_dict_updated)
        print(user_for_log_updated.email)
        print(user_for_log_updated.password)

        





        
