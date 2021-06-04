import datetime

from pytz import timezone

_tz = timezone("US/Eastern")


def format_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return _tz.localize(obj.replace(microsecond=0)).isoformat()
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, str):
        return obj
    else:
        return None


def local_time_now():
    return _tz.localize(datetime.datetime.now())
