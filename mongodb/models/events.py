import json
import re
import datetime
from mongodb.models.users import User
from mongodb.models.tags import Tag
import mongoengine as me
from mongodb.utils import flatten_id_field


class Event(me.Document):
    artist_id = me.ReferenceField('User')
    tour = me.StringField(max_length=50, required=True)
    date = me.StringField(
        regex=re.compile(
            '^([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]'
            + '([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2})$'
        )
    )
    time = me.StringField(
        regex=re.compile('^(?:2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$')
    )
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
            date,
            time,
            sold_out=False,
            came_from_request_id=False,
            tags=[],
            featured=False,
            deleted=False,
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
        event.date = date
        event.time = time
        event.tags = tags
        event.featured = featured
        event.deleted = deleted
        event.save()
        return event

    @classmethod
    def get_future_events(cls, size, page_num, artist, city, when, tags):
        # until_when = get_date_filter(when)
        filters = {
            'city__icontains': city,
            # 'date__gte': datetime.datetime.now(),
            # 'date__lte': until_when
        }

        if artist:
            filters['artist_id__in'] = User.objects(
                name__icontains=artist,
                is_artist=True
            )
        if tags:
            filters['tags__all'] = Tag.objects(id__in=tags)

        featured_event = cls.objects(featured=True).first()
        events_queryset = cls.objects(**filters)[(page_num - 1) * size:page_num * size]
        events_dicts_list = json.loads(events_queryset.to_json())
        events_dicts_list_results = []

        events_dicts_list = flatten_id_field(events_dicts_list)
        
        for event in events_dicts_list:
            event['artist'] = \
                User.objects(id=event['artist_id']['$oid']).only('name').first()['name']

            event_date = datetime.datetime.strptime(event['date'], "%d/%m/%Y").date()
            if event_date >= datetime.datetime.now().date(): # make this more effecient by defining a date object in the db
                events_dicts_list_results.append(event)


        return {'featured': json.loads(featured_event.to_json()), 'events': events_dicts_list_results}

    @classmethod
    def get_past_events(cls):
        events_queryset = cls.objects()
        events_dicts_list = json.loads(events_queryset.to_json())
        past_events = []
        for event in events_dicts_list:
            event_date = datetime.datetime \
                .strptime(event['date'], "%d/%m/%Y").date()
            if event_date < datetime.datetime.now().date():
                past_events.append(event)
        return {'events': past_events}

    @classmethod
    def get_event_by_id(cls, event_id):
        event = cls.objects(id=event_id).first()
        event_dict = json.loads(event.to_json())
        event_dict['artist'] = \
            User.objects(id=event_dict['artist_id']['$oid']) \
                .only('name').first()['name']

        return event_dict

    @classmethod
    def get_events_of_artist(cls, artist_id):
        events_of_artist = cls.objects(artist_id=artist_id)
        events_dict = json.loads(events_of_artist.to_json())
        for event in events_dict:
            event['artist'] = \
                User.objects(id=event['artist_id']['$oid']).only('name').first()['name']

        return events_dict

    meta = {
        'collection': 'events',
    }
