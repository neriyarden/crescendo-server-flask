import json
import os
import mongodb.mongo_setup as mongo_setup
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
from mongodb.models.users import User
from env import config_env_vars
from datetime import datetime

app = Flask(__name__)


with app.app_context():
    config_env_vars()
    mongo_setup.global_init()


@app.route('/artists')
def getArtists():
    size = request.args.get('size') or 25
    page_num = request.args.get('pageNum') or 0
    starts_with = request.args.get('startsWith') or ''
    search_term = request.args.get('searchTerm') or ''
    artists = User.get_all_artists(size, page_num, starts_with, search_term)
    return artists.to_json()


@app.route('/artists/<string:artist_id>')
def getArtist(artist_id):
    artist = User.get_artist_by_id(artist_id)
    return artist.to_json()


if __name__ == '__main__':
    app.run(port=5000, debug=True) # turn off debug for production

# password_hash = generate_password_hash("ny123456!")

# auth = HTTPBasicAuth()
# app.config['PASSWORD_HASH'] = os.environ.get('PASSWORD_HASH', password_hash)

# @auth.verify_password
# def verify_password(username, password):
#     return check_password_hash(app.config['PASSWORD_HASH'], password)

# @auth.error_handler
# def unauthorized():
#     return jsonify(error='unauthorized access'), 403

# @app.route('/signin')
# @auth.login_required
# def hello():
#     return "Hello World!"





# artist_data = reqparse.RequestParser()

# artist_data.add_argument(
#     'artist_id', type=str, help='The artist id is required', required=True
# )
# artist_data.add_argument(
#     'bio', type=str, help='Biography of the artist'
# )
# artist_data.add_argument(
#     'link_to_spotify', type=str, help='Link to artist spotify'
# )
# artist_data.add_argument(
#     'link_to_instagram', type=str, help='Link to artist instagram'
# )
# artist_data.add_argument(
#     'link_to_facebook', type=str, help='Link to artist facebook'
# )
# artist_data.add_argument(
#     'link_to_youtube', type=str, help='Link to artist youtube'
# )

# class Artists(Resource):
#     def get(self):
#         """Get all artists data"""
#         args = artist_data.parse_args()
#         return args

# api.add_resource(Artists, '/artists')



# class Artist(Resource):
#     def get(self, artist_id=None):
#         """Get artist data"""
#         if not artist_id:
#             abort(400, message='No artist id was given')

#         # if artist_id doesn't exist:
#             # abort(404, message='Artist id doesn\'t exist')

#         # Get artist data by id

#         # Get all events of artist by id

#         # Get all requests of artist by id


#     def put(self, artist_id):
#         """Update artist data"""
#         args = artist_data.parse_args()
#         return 'put'
#         # return {"artist_data": args}, 201


# api.add_resource(Artist, '/artist/<string:artist_id>')








