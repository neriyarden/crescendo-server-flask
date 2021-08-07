import os

from flask import Blueprint, flash, request
from mongodb.models.users import User
from werkzeug.utils import secure_filename

Artists = Blueprint('Artists', __name__)


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
    return artists.to_json()


# get artist data by id
@Artists.route('/artists/<string:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = User.get_artist_by_id(artist_id)
    return artist.to_json()


# finish this
@Artists.route('/artists', methods=['PATCH'])
def update_artist():
    file = request.files.get('file')
    user_id = request.form.get('user_id')
    link_to_spotify = request.form.get('link_to_spotify')
    link_to_instagram = request.form.get('link_to_instagram')
    link_to_facebook = request.form.get('link_to_facebook')
    link_to_youtube = request.form.get('link_to_youtube')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(Artists.config['ARTISTS_IMG_FOLDER'], filename))

    return 'asdljhgadlfiugauiuehqwpeur889'
