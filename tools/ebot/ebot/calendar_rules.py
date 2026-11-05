"""Local gates for Massive Stocks Basic history and the next-day cutoff.

These checks do not contact the network. They are not an exchange holiday calendar.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.9 stdlib provides zoneinfo
    ZoneInfo = None  # type: ignore

BASIC_HISTORY_DAYS = 731
NEW_YORK = "America/New_York"


def session_access(session: date, now: datetime) -> str:
    """Return ACCESSIBLE or a local reason not to call Massive.

    Basic grouped daily bars for a session become available after midnight
    America/New_York on the following calendar day. Weekends are not sessions.
    Exchange holidays are not classified here.
    """
    if session.weekday() >= 5:
        return "NOT_A_WEEKDAY_SESSION"
    if ZoneInfo is None:
        return "TIMEZONE_DATA_MISSING"
    try:
        zone = ZoneInfo(NEW_YORK)
    except Exception:
        return "TIMEZONE_DATA_MISSING"
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    now_local = now.astimezone(zone)
    available_at = datetime.combine(
        session + timedelta(days=1), time.min, tzinfo=zone
    )
    if now_local < available_at:
        return "NOT_YET_ACCESSIBLE_ON_BASIC"
    return "ACCESSIBLE"


def history_window_ok(from_date: date, session: date) -> bool:
    """True when the inclusive span fits the published Basic two-year window.

    This is a local guard, not proof of the account's entitlement.
    """
    if from_date >= session:
        return False
    return (session - from_date).days <= BASIC_HISTORY_DAYS
