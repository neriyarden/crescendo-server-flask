import datetime


def get_date_filter(when):
    if not when:
        return datetime.datetime.now() + datetime.timedelta(days=365)
    date_filters = {
        'today': datetime.datetime.now() + datetime.timedelta(days=1),
        'thisWeek': datetime.datetime.now() + datetime.timedelta(days=7),
        'thisMonth': datetime.datetime.now() + datetime.timedelta(days=30),
        'all': datetime.datetime.now() + datetime.timedelta(days=365)
    }
    return date_filters[when]