from flask import request, Blueprint, Response
from mongodb.models.events import Event
import json


Events = Blueprint('Events', __name__)


# get Events data with filters
@Events.route('/events', methods=['GET'])
def get_events():
    size        = request.args.get('size') or 25
    page_num    = request.args.get('pageNum') or 1
    artist = request.args.get('artist') or ''
    city = request.args.get('city') or ''
    when = request.args.get('when') or ''
    tags = request.args.getlist('tags') or []
    
    if when != 'past':
        events = Event.get_future_events(int(size), int(page_num), artist, city, when, tags)
    if when == 'past':
        events = Event.get_past_events()
    resp = Response(json.dumps(events), status=200, mimetype='application/json')
    return resp


@Events.route('/events/<string:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    event = Event.get_event_by_id(event_id)
    resp = Response(json.dumps(event), status=200, mimetype='application/json')
    return resp


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

