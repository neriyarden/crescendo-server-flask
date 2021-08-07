import datetime
import mongoengine as me
from mongodb.models.users import User


class Event(me.Document):
    artist_id = me.ReferenceField('User', DBRef=True)
    tour = me.StringField(max_length=50, required=True)
    datetime = me.DateTimeField()
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
            artist_id,
            duration,
            venue,
            city,
            tour,
            description,
            img_url,
            ticketseller_url,
            datetime,
            sold_out = False,
            came_from_request_id = False,
            tags = [],
            featured = False,
            deleted = False,
            ):
        """"""
        event = cls()
        event.artist_id = artist_id
        event.duration = duration
        event.venue = venue
        event.city = city
        event.tour = tour
        event.description = description
        event.img_url = img_url
        event.ticketseller_url = ticketseller_url
        event.sold_out = sold_out
        event.came_from_request_id = came_from_request_id
        event.datetime = datetime
        event.tags = tags
        event.featured = featured
        event.deleted = deleted
        event.save()
        return event

    meta = {
        'collection': 'events',
    }
