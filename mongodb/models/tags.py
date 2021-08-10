import mongoengine as me
import json

class Tag(me.Document):
    name = me.StringField(max_length=20, required=True, unique=True)

    @classmethod
    def create_tag(cls, name):
        """"""
        tag = cls()
        tag.name = name
        tag.save()
        return tag

    @classmethod
    def get_tags(cls):
        tags_queryset = cls.objects()
        tags_dicts_list = json.loads(tags_queryset.to_json())

        for tag in tags_dicts_list:
            tag['id'] = tag['_id']['$oid']
            del tag['_id']

        return tags_dicts_list

    meta = {
        'collection': 'tags'
    }