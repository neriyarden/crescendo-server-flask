import datetime
from os import startfile
from typing import Sequence

import mongoengine as me
import json

from mongodb.utils import flatten_id_field, normalize_date_field

class User(me.Document):
    # id = SequenceField()
    name = me.StringField(max_length=50, required=True, unique=True)
    email = me.EmailField(max_length=50, required=True, unique=True)
    password = me.StringField(max_length=50, required=True)
    joined_at = me.DateTimeField(default=datetime.datetime.now)
    votes = me.ListField(me.DictField())
    is_artist = me.BooleanField(default=False)

    @classmethod
    def create_account(cls, name, email, password, is_artist, *args, **kwargs):
        """"""
        user = Artist(*args, **kwargs) if is_artist else cls()
        user.name = name
        user.email = email
        user.password = password
        user.is_artist = is_artist
        user.save()
        return user

    @classmethod
    def get_all_artists(cls, size, page_num, starts_with, search_term):
        """"""
        artists = cls.objects(
            name__istartswith=starts_with,
            name__icontains=search_term,
            is_artist=True
        )[(page_num - 1) * size:page_num * size]
        return artists

    @classmethod
    def get_artist_by_id(cls, id):
        """"""
        artist = cls.objects(id=id).first()
        artist_dict = json.loads(artist.to_json())
        artist_dict['joined_at'] = artist.joined_at.isoformat()[:10]
        return flatten_id_field(artist_dict)

    @classmethod
    def validate_user(cls, email, password):
        """"""
        existing_user = cls.objects(email=email, password=password).first()
        return existing_user

    @classmethod
    def get_user_details(cls, user_id):
        """"""
        user_details = cls.objects(id=user_id).first()
        return user_details


    meta = {
        'collection': 'users',
        'indexes': [('name','email')],
        'allow_inheritance': True
    }
    

class Artist(User):
    img_url = me.StringField(max_length=255)
    bio = me.StringField(max_length=1000)
    link_to_spotify = me.StringField(max_length=255)
    link_to_instagram = me.StringField(max_length=255)
    link_to_facebook = me.StringField(max_length=255)
    link_to_youtube = me.StringField(max_length=255)
