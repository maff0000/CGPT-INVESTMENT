"""Synthetic bars for offline tests. These are not market data."""

from datetime import date, datetime, timedelta, timezone

SENTINEL_PRICE = 888888.88
SENTINEL_VOLUME = 42424242


def weekdays_ending(session, count):
    days = []
    cursor = session
    while len(days) < count:
        if cursor.weekday() < 5:
            days.append(cursor)
        cursor -= timedelta(days=1)
    days.reverse()
    return days


def bar(day, price=SENTINEL_PRICE, volume=SENTINEL_VOLUME):
    stamp = int(datetime(day.year, day.month, day.day, tzinfo=timezone.utc).timestamp() * 1000)
    return {
        "t": stamp,
        "o": price,
        "h": price + 1,
        "l": price - 1,
        "c": price,
        "v": volume,
    }


def series(session, count):
    day = session if isinstance(session, date) else date.fromisoformat(session)
    return [bar(item) for item in weekdays_ending(day, count)]
