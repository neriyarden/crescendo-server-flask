import datetime
import mongoengine as me


class User(me.Document):
    name = me.StringField(max_length=50, required=True, unique=True)
    email = me.EmailField(max_length=50, required=True, unique=True)
    password = me.StringField(max_length=50, required=True)
    joined_at = me.DateTimeField(default=datetime.datetime.utcnow)
    votes = me.ListField(me.DictField())
    is_artist = me.BooleanField(default=False)

    @classmethod
    def create_account(cls, name, email, password, is_artist = False, *args, **kwargs):
        """"""
        user = Artist(*args, **kwargs) if is_artist else cls()
        user.name = name
        user.email = email
        user.password = password
        user.is_artist
        user.save()
        return user

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
    events = me.ListField(me.ReferenceField('Event'))
    requests = me.ListField(me.ReferenceField('Request'))