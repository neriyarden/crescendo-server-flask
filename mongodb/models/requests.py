import json

from flask.globals import request
from mongodb.utils import flatten_id_field
from mongodb.models.users import User
import datetime
import mongoengine as me

class Request(me.Document):
    artist_id = me.ReferenceField('User')
    tour = me.StringField(max_length=50, required=True)
    requested_at = me.DateTimeField(default=datetime.datetime.utcnow)
    city = me.StringField(max_length=50, required=True)
    cap = me.IntField(min_value=1)
    
    @classmethod
    def create_request(cls, artist_id, tour, city, cap):
        """"""
        request = cls()
        request.artist_id = artist_id
        request.tour = tour
        request.city = city
        request.cap = cap
        request.save()
        return request

    @classmethod
    def get_requests(cls, size, page_num, artist, city):
        filters = {
            'city__icontains': city,
        }

        if artist:
            filters['artist_id__in'] = User.objects(
                name__icontains=artist,
                is_artist=True
            )
        requests_queryset = cls.objects(**filters)[(page_num - 1) * size:page_num * size]
        requests_dicts_list = json.loads(requests_queryset.to_json())

        requests_dicts_list = flatten_id_field(requests_dicts_list)
        
        for request in requests_dicts_list:
            request_artist = User.objects(id=request['artist_id']['$oid']).first()
            request['artist'] = request_artist['name']
            request['img_url'] = request_artist['img_url']
            request['votes'] = User.objects(votes=request).count() #.to_json())

        return requests_dicts_list

    @classmethod
    def cast_vote(cls, request_id, user_id):
        request_queryset = Request.objects(id=request_id).first()
        print('2', request_queryset)
        user_queryset = User.objects(id=user_id)
        user_queryset.update_one(push__votes=request_queryset)
        return user_queryset


    meta = {
        'collection': 'requests',
    }


        # request_queryset = cls.objects(id=request_id)
        # request_queryset.update_one(push__votes=user)
        # return request_queryset