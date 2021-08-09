import os
import json
from flask import Blueprint, request, Response
from mongodb.models.users import User
from werkzeug.utils import secure_filename

Users = Blueprint('Users', __name__)


# create_account
@Users.route('/users', methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    repeat_password = request.json['repeat_password']
    is_artist = bool(request.json['is_artist'])
    artist_fields = {
        'img_url': '',
        'bio': '',
        'link_to_spotify': '',
        'link_to_instagram': '',
        'link_to_facebook': '',
        'link_to_youtube': ''
    }

    if password != repeat_password:
        return Response(
            json.dumps({'error': 'Passwords don\'t match'}),
            400,
            mimetype='application/json'
            )

    new_user = User.create_account(
        name, email, password, is_artist, **artist_fields
        )
    return Response(
        new_user.to_json(),
        200,
        mimetype='application/json'
        )
