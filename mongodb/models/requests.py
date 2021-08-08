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

    meta = {
        'collection': 'requests'
    }