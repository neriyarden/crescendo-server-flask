from mongodb.models.events import Event
from mongodb.models.users import User
from datetime import datetime
from mongodb.models.tags import Tag


"""Dummy data for the db"""

def insert_dummydata():
    # tags
    solo = Tag.objects(id='6106b98db94c8b55f3b5e8ae').first()
    acoustic = Tag.objects(id='6106b98db94c8b55f3b5e8af').first()
    party = Tag.objects(id='6106b98db94c8b55f3b5e8b0').first()
    intimate = Tag.objects(id='6106b98db94c8b55f3b5e8b1').first()
    loud = Tag.objects(id='6106b98db94c8b55f3b5e8b2').first()
    adults_only = Tag.objects(id='6106b98eb94c8b55f3b5e8b3').first()
    kids = Tag.objects(id='6106b98eb94c8b55f3b5e8b4').first()
    sitting = Tag.objects(id='6106b98eb94c8b55f3b5e8b5').first()
    standing = Tag.objects(id='6106b98eb94c8b55f3b5e8b6').first()
    accessible = Tag.objects(id='6106b98eb94c8b55f3b5e8b7').first()
    electronic = Tag.objects(id='6106b98eb94c8b55f3b5e8b8').first()
    full_band = Tag.objects(id='6106b98eb94c8b55f3b5e8b9').first()

    joe_mayor = User.objects(id='6106ae3b69972d00690ff294').first()
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 8, 7).strftime("%d/%m/%Y"),
        # https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
        time=datetime.time(23).strftime("%H:%M:%S"),
        tags=[solo, loud, accessible, standing]
    )
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 8, 20).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[solo, acoustic, electronic, sitting]
    )
    Event.create_event(
        artist_id=joe_mayor,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='הצוללת הצהובה',
        city='Jerusalem',
        description='wow amazing cool',
        img_url='img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 9, 21).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[full_band, kids, intimate, party]
    )

    allou_neder = User.objects(id='6106ae3b69972d00690ff295').first()
    Event.create_event(
        artist_id=allou_neder,
        tour='Allóu Neder Israel Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 9, 16).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[solo, kids, sitting, party]
    )
    Event.create_event(
        artist_id=allou_neder,
        tour='Allóu Neder Israel Tour',
        duration=90,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 7, 25).strftime("%d/%m/%Y"),
        time=datetime.time(20).strftime("%H:%M:%S"),
        tags=[loud, party, adults_only, full_band, standing]
    )

# 1('Zappa Haifa', 1, 'Flieman St 2-8, Haifa, 3508415'),
# 2('Barby', 2, 'Kibbutz Galuyot Rd 52, Tel Aviv-Yafo'),
# 3('הצוללת הצהובה', 3, 'Ha-Rekhavim St 13, Jerusalem, 9346212'),
# 4('Heychal Hatarbut', 4, 'Kibbutz Galuyot Rd 52, Afula'),
# 5('Amphi Ashdod', 5, 'Mafkura St, Ashdod'),
# 6('Papa Pizza', 6, 'Jerusalem Ave 24, Beit Shean')
