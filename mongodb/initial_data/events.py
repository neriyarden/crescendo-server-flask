import mongodb.mongo_setup as mongo_setup
from mongodb.models.events import Event
from mongodb.models.users import User
# from mongoengine import ObjectId
from datetime import datetime


"""Dummy data for the db"""


def insert_dummydata():
    joe_mayor = User.objects(id='6106ae3b69972d00690ff294').first()
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        datetime=datetime(2021, 7, 4, hour=23)
    )
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        datetime=datetime(2021, 7, 6, hour=22)
    )
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='הצוללת הצהובה',
        city='Jerusalem',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        datetime=datetime(2021, 8, 7, hour=22)
    )

    allou_neder = User.objects(id='6106ae3b69972d00690ff295').first()
    Event.create_event(
        artist_id=allou_neder,
        tour='Allóu Neder Israel Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='/img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        datetime=datetime(2021, 9, 16, hour=22)
    )
    Event.create_event(
        artist_id=allou_neder,
        tour='Allóu Neder Israel Tour',
        duration=90,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='/img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        datetime=datetime(2021, 7, 25, hour=20)
    )

# 1('Zappa Haifa', 1, 'Flieman St 2-8, Haifa, 3508415'),
# 2('Barby', 2, 'Kibbutz Galuyot Rd 52, Tel Aviv-Yafo'),
# 3('הצוללת הצהובה', 3, 'Ha-Rekhavim St 13, Jerusalem, 9346212'),
# 4('Heychal Hatarbut', 4, 'Kibbutz Galuyot Rd 52, Afula'),
# 5('Amphi Ashdod', 5, 'Mafkura St, Ashdod'),
# 6('Papa Pizza', 6, 'Jerusalem Ave 24, Beit Shean')
