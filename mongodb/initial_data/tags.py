import mongodb.mongo_setup as mongo_setup
from mongodb.models.tags import Tag


"""Dummy data for the db"""

# mongo_setup.global_init()

def insert_dummydata():
    Tag.create_tag('Solo')
    Tag.create_tag('Acoustic')
    Tag.create_tag('Party')
    Tag.create_tag('Intimate')
    Tag.create_tag('Loud')
    Tag.create_tag('18+')
    Tag.create_tag('Kids')
    Tag.create_tag('Sitting')
    Tag.create_tag('Standing')
    Tag.create_tag('Accessible')
    Tag.create_tag('Electronic')
    Tag.create_tag('Full Band')