from flask import request, Blueprint, Response
from mongodb.models.users import User
import json


Sign_in = Blueprint('Sign_in', __name__)

@Sign_in.route('/signIn', methods=['POST'])
def sign_in():
    email = request.json['email']
    password = request.json['password']
    validated_user = User.validate_user(email, password)
    print(validated_user)
    if not validated_user:
        return Response(
            json.dumps({'error': 'Incorrect email or password'}),
            status=404,
            mimetype='application/json'
        )
    resp = Response(validated_user.to_json(), status=200, mimetype='application/json')
    resp.set_cookie('session_id', str(validated_user.id))
    return resp