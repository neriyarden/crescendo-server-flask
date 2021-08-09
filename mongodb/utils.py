import datetime
import json


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


def flatten_id_field(results):
    if type(results) == list:
        results = [results]
        for res in results:
            res['id'] = res['_id']['$oid']
            del res['_id']

    if type(results) == dict:
        results['id'] = results['_id']['$oid']
        del results['_id']

    return results


def normalize_date_field(results, fieldName):
    if type(results) == list:
        results = [results]
        for res in results:
            res[fieldName] = res[fieldName]['$date']

    if type(results) == dict:
        results[fieldName] = results[fieldName]['$date'].isoformat()
    return results