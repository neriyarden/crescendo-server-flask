from flask import request, Blueprint
from mongodb.models.users import User


Events = Blueprint('Events', __name__)




# get Events data with filters
@Events.route('/events', methods=['GET'])
def get_events():
    size        = request.args.get('size') or 25
    page_num    = request.args.get('pageNum') or 0
#     starts_with = request.args.get('startsWith') or ''
#     search_term = request.args.get('searchTerm') or ''
    
#     artists = User.get_all_artists(size, page_num, starts_with, search_term)
#     return artists.to_json()


# get artist data by id
# @Events.route('/events/<string:artist_id>', methods=['GET'])
# def get_artist(artist_id):
#     artist = User.get_artist_by_id(artist_id)
#     return artist.to_json()


# finish this
# @Events.route('/events/', methods=['PATCH'])
# def update_artist():
#     request.file.get('newImg')
#     request.form.get('user_id')
#     request.form.get('link_to_spotify')
#     request.form.get('link_to_instagram')
#     request.form.get('link_to_facebook')
#     request.form.get('link_to_youtube')

