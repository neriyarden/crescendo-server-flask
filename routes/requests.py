from flask import request, Blueprint, Response
from mongodb.models.requests import Request

import json


Requests = Blueprint('Requests', __name__)


# get Requests data with filters
@Requests.route('/requests', methods=['GET'])
def get_requests():
    size        = request.args.get('size') or 25
    page_num    = request.args.get('pageNum') or 1
    artist = request.args.get('artist') or ''
    city = request.args.get('city') or ''
    
    requests = Request.get_requests(int(size), int(page_num), artist, city)
    resp = Response(json.dumps(requests), status=200, mimetype='application/json')
    return resp


@Requests.route('/requests/<string:request_id>', methods=['GET'])
def get_request_by_id(request_id):
    request = Request.get_request_by_id(request_id)
    return Response(request, 200, mimetype='application/json')


@Requests.route('/requests/<string:request_id>/vote/<string:user_id>', methods=['POST'])
def cast_vote(request_id, user_id):
    updated_request = Request.cast_vote(request_id, user_id)
    # if not updated_request:
    return Response(
        json.dumps({'msg': 'Vote submitted successfully'}),
        200,
        mimetype='application/json'
        )