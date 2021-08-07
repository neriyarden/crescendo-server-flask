from flask import request, Blueprint
from mongodb.models.events import Event


Events = Blueprint('Events', __name__)




# get Events data with filters
@Events.route('/events', methods=['GET'])
def get_events():
    size        = int(request.args.get('size')) or 25
    page_num    = int(request.args.get('pageNum')) or 0
    artist = request.args.get('artist') or ''
    city = request.args.get('city') or ''
    when = request.args.get('when') or ''
    tags = request.args.get('tags') or []
    
    events = Event.get_future_events(size, page_num, artist, city, when, tags)
    return events.to_json()


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

