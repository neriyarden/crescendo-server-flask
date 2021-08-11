from mongodb.models.requests import Request
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

@Users.route('/users/<string:user_id>', methods=['get'])
def get_user(user_id):
    user_details = User.get_user_details(user_id)
    if not user_details:
        return Response('No results', 404, mimetype='application/json')
    return Response(user_details.to_json(), 200, mimetype='application/json')


@Users.route('/users/<string:user_id>/votes', methods=['get'])
def get_user_votes(user_id):
    user_votes = User.get_user_votes(user_id)
    for vote in user_votes:
        request_json = Request.get_request_by_id(vote['request_id'])
        request_dict = json.loads(request_json)
        vote.update(request_dict)
        # vote['artist_id'] = vote['artist_id']['$oid']
        vote['artist'] = User.get_artist_name(vote['artist_id'])
        del vote['$oid']

    return Response(json.dumps(user_votes), 200, mimetype='application/json')

