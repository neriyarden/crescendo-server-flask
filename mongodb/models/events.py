import datetime
import mongoengine as me


class Event(me.Document):
    artist_id = me.ReferenceField('User')
    tour = me.StringField(max_length=50, required=True)
    datetime = me.DateTimeField(default=datetime.datetime.utcnow)
    duration = me.IntField(min_value=20)
    venue = me.StringField(max_length=50, required=True)
    city = me.StringField(max_length=50, required=True)
    description = me.StringField(max_length=200)
    img_url = me.StringField(max_length=255)
    came_from_request_id = me.BooleanField(default=False)
    ticketseller_url = me.StringField(max_length=255)
    tags = me.ListField(me.ReferenceField('Tag'))
    sold_out = me.BooleanField(default=False)
    featured = me.BooleanField(default=False)
    deleted = me.BooleanField(default=False)

    @classmethod
    def create_event(
            cls,
            artist,
            datetime,
            duration,
            venue,
            city,
            tour,
            description,
            img_url,
            ticketseller_url,
            sold_out = False,
            came_from_request_id = False,
            tags = [],
            featured = False,
            deleted = False,
            ):
        """"""
        request = cls()
        request.artist = artist
        request.datetime = datetime
        request.duration = duration
        request.city = city
        request.cap = cap
        request.save()
        return request

    meta = {
        'collection': 'events'
    }
