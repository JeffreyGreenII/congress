import datetime


def current_congress():
    year = current_legislative_year()
    return congress_from_legislative_year(year)


def congress_from_legislative_year(year):
    return ((year + 1) // 2) - 894


def current_legislative_year(date=datetime.datetime.now()):
    if date.month == 1:
        if date.day == 1 or date.day == 2:
            return date.year - 1
        elif date.day == 3 and date.hour < 12:
            return date.year - 1
        else:
            return date.year
    else:
        return date.year


def get_congress_first_year(congress):
    return ((int(congress) + 894) * 2) - 1


def get_congress_years(congress):
    y1 = get_congress_first_year(congress)
    return (y1, y1 + 1, y1 + 2)
