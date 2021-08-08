from flask import request, Blueprint, Response
from mongodb.models.tags import Tag
import json


Tags = Blueprint('Tags', __name__)


@Tags.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.get_tags()
    resp = Response(json.dumps(tags), status=200, mimetype='application/json')
    return resp
