"""Validate daily bars without retaining prices for the report."""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

MIN_BARS = 260
_LONG_GAP = 4


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _utc_day(timestamp_ms: object) -> str:
    if not _is_number(timestamp_ms):
        raise ValueError("timestamp")
    millis = float(timestamp_ms)
    if millis < 10**12 or millis > 10**14:
        raise ValueError("timestamp")
    return datetime.fromtimestamp(millis / 1000.0, timezone.utc).strftime("%Y-%m-%d")


def bar_is_invalid(bar: object) -> bool:
    if not isinstance(bar, dict):
        return True
    try:
        _utc_day(bar.get("t"))
    except (ValueError, OSError, OverflowError):
        return True
    required = ("o", "h", "l", "c", "v")
    if not all(_is_number(bar.get(field)) for field in required):
        return True
    open_ = float(bar["o"])
    high = float(bar["h"])
    low = float(bar["l"])
    close = float(bar["c"])
    volume = float(bar["v"])
    if min(open_, high, low, close) <= 0 or volume < 0:
        return True
    if high < low or high < open_ or high < close or low > open_ or low > close:
        return True
    return False


def _longest_weekday_run(missing: list[str]) -> int:
    if not missing:
        return 0
    best = 1
    run = 1
    for previous, current in zip(missing, missing[1:]):
        before = date.fromisoformat(previous)
        after = date.fromisoformat(current)
        expected = before + timedelta(days=1)
        while expected.weekday() >= 5:
            expected += timedelta(days=1)
        if after == expected:
            run += 1
            best = max(best, run)
        else:
            run = 1
    return best


def weekday_gaps(session_days: list[str]) -> list[str]:
    """Weekdays between the first and last returned session that have no bar.

    Exchange holidays are not identified. Callers must not treat this list as
    a confirmed corporate or market calendar.
    """
    if not session_days:
        return []
    start = date.fromisoformat(min(session_days))
    end = date.fromisoformat(max(session_days))
    present = set(session_days)
    missing = []
    cursor = start
    while cursor <= end:
        if cursor.weekday() < 5 and cursor.isoformat() not in present:
            missing.append(cursor.isoformat())
        cursor += timedelta(days=1)
    return missing


def summarise_bars(results: object) -> dict:
    """Count and check bars. The returned dict has no prices and no raw rows."""
    summary = {
        "daily_records": 0,
        "unique_sessions": 0,
        "earliest": "NONE",
        "latest": "NONE",
        "duplicate_records": 0,
        "invalid_records": 0,
        "ordered": "yes",
        "possible_missing_weekdays": 0,
        "possible_missing_weekday_dates": [],
        "long_weekday_gap": "no",
        "coverage_260": "HOLD",
    }
    if not isinstance(results, list):
        summary["invalid_records"] = 1
        summary["ordered"] = "no"
        return summary
    summary["daily_records"] = len(results)
    days = []
    previous = None
    seen = set()
    for bar in results:
        if bar_is_invalid(bar):
            summary["invalid_records"] += 1
            summary["ordered"] = "no"
            continue
        day = _utc_day(bar["t"])
        millis = float(bar["t"])
        if previous is not None and millis < previous:
            summary["ordered"] = "no"
        previous = millis
        if day in seen:
            summary["duplicate_records"] += 1
        seen.add(day)
        days.append(day)
    summary["unique_sessions"] = len(seen)
    if days:
        summary["earliest"] = min(days)
        summary["latest"] = max(days)
        gaps = weekday_gaps(days)
        summary["possible_missing_weekdays"] = len(gaps)
        summary["possible_missing_weekday_dates"] = gaps[:15]
        if _longest_weekday_run(gaps) >= _LONG_GAP:
            summary["long_weekday_gap"] = "yes"
    if (
        summary["unique_sessions"] >= MIN_BARS
        and summary["duplicate_records"] == 0
        and summary["invalid_records"] == 0
        and summary["ordered"] == "yes"
        and summary["long_weekday_gap"] == "no"
    ):
        summary["coverage_260"] = "PASS"
    return summary
