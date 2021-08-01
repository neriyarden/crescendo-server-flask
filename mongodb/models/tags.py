import mongoengine as me

class Tag(me.Document):
    name = me.StringField(max_length=20, required=True, unique=True)

    @classmethod
    def create_tag(cls, name):
        """"""
        tag = cls()
        tag.name = name
        tag.save()
        return tag

    meta = {
        'collection': 'tags'
    }