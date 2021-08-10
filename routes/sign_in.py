from flask import request, Blueprint, Response
from flask.helpers import make_response
from mongodb.models.users import User
import json


Sign_in = Blueprint('Sign_in', __name__)

@Sign_in.route('/signIn', methods=['POST'])
def sign_in():
    email = request.json['email']
    password = request.json['password']
    validated_user = User.validate_user(email, password)
    if not validated_user:
        return Response(
            json.dumps({'error': 'Incorrect email or password'}),
            status=403,
            mimetype='application/json'
        )
    resp = Response(validated_user.to_json(), status=200, mimetype='application/json')
    # resp1 = make_response(validated_user.to_json())
    resp.set_cookie('session_id', str(validated_user.id))
    return resp