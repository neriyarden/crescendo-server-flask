from flask import request
from flask import Blueprint
from mongodb.models.users import User


Artists = Blueprint('Artists', __name__)


@Artists.route('/artists')
def getArtists():
    size        = request.args.get('size') or 25
    page_num    = request.args.get('pageNum') or 0
    starts_with = request.args.get('startsWith') or ''
    search_term = request.args.get('searchTerm') or ''
    
    artists = User.get_all_artists(size, page_num, starts_with, search_term)
    return artists.to_json()


@Artists.route('/artists/<string:artist_id>')
def getArtist(artist_id):
    artist = User.get_artist_by_id(artist_id)
    return artist.to_json()
