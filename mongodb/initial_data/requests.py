import mongodb.mongo_setup as mongo_setup
from mongodb.models.requests import Request
from mongodb.models.users import User
from datetime import datetime


"""Dummy data for the db"""


def insert_dummydata():
    joe_mayor = User.objects(id='6106ae3b69972d00690ff294').first()
    Request.create_request(
        user_id = joe_mayor,
        tour = 'Joe Mayor World Tour',
        city = 'Afula',
        cap = 1200
    )

    allou_neder = User.objects(id='6106ae3b69972d00690ff295').first()
    Request.create_request(
        user_id = allou_neder,
        tour = 'Allóu Neder Israel Tour',
        city = 'Jerusalem',
        cap = 1400
    )
