from mongodb.models.events import Event
from mongodb.models.requests import Request
import os
import json

from flask import Blueprint, request, Response
from mongodb.models.users import User
from mongodb.models.events import Event
from werkzeug.utils import secure_filename


Artists = Blueprint('Artists', __name__)
ARTISTS_IMG_FOLDER = '/img/artists'
ALLOWED_EXTENSIONS = {'jfif', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# get artists data with filters
@Artists.route('/artists', methods=['GET'])
def get_artists():
    size        = request.args.get('size') or 25
    page_num    = request.args.get('pageNum') or 1
    starts_with = request.args.get('startsWith') or ''
    search_term = request.args.get('searchTerm') or ''
    
    artists = User.get_all_artists(int(size), int(page_num), starts_with, search_term)
    resp = Response(artists.to_json(), status=200, mimetype='application/json')
    return resp


# get artist data by id
@Artists.route('/artists/<string:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist_details = User.get_artist_by_id(artist_id)
    if not artist_details:
        return Response('No results', 404, mimetype='application/json')
    resp = Response(json.dumps(artist_details), status=200, mimetype='application/json')
    return resp


@Artists.route('/artists/<string:artist_id>/events', methods=['GET'])
def get_events_of_artist(artist_id):
    artist_events = Event.get_events_of_artist(artist_id)
    if not artist_events:
        return Response('No results', 404, mimetype='application/json')
    resp = Response(json.dumps(artist_events), status=200, mimetype='application/json')
    return resp


@Artists.route('/artists/<string:artist_id>/requests', methods=['GET'])
def get_requests_of_artist(artist_id):
    artist_requests = Request.get_requests_of_artist(artist_id)
    if not artist_requests:
        return Response('No results', 404, mimetype='application/json')
    resp = Response(artist_requests, status=200, mimetype='application/json')
    return resp

@Artists.route('/artists', methods=['PATCH'])
def edit_artist_data():
    file = request.files.get('newImg')
    user_id = request.form.get('user_id')
    bio = request.form.get('bio')
    link_to_spotify = request.form.get('link_to_spotify')
    link_to_instagram = request.form.get('link_to_instagram')
    link_to_facebook = request.form.get('link_to_facebook')
    link_to_youtube = request.form.get('link_to_youtube')
    filename = None
    if file and allowed_file(file.filename):
        filename = os.path.join(
            ARTISTS_IMG_FOLDER.lstrip('/'),
            secure_filename(file.filename)
        )
        file.save(filename)
    updated_user = User.edit_artist_data(
        user_id,
        bio,
        link_to_spotify,
        link_to_instagram,
        link_to_facebook,
        link_to_youtube,
        filename
        )
    return Response(updated_user, 200, mimetype='application/json')