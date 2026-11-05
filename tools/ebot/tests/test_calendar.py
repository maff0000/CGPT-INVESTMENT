"""Basic-plan clock and history window. No network."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401
from datetime import datetime, timezone

from ebot.calendar_rules import history_window_ok, session_access
from ebot.massive import parse_iso_date


class CalendarTests(unittest.TestCase):
    def test_basic_cutoff_in_eastern_standard_time(self):
        session = parse_iso_date("2026-11-04")
        before = datetime(2026, 11, 5, 4, 59, tzinfo=timezone.utc)
        at_midnight = datetime(2026, 11, 5, 5, 0, tzinfo=timezone.utc)
        self.assertEqual(session_access(session, before), "NOT_YET_ACCESSIBLE_ON_BASIC")
        self.assertEqual(session_access(session, at_midnight), "ACCESSIBLE")

    def test_basic_cutoff_in_eastern_daylight_time(self):
        session = parse_iso_date("2026-07-02")
        before = datetime(2026, 7, 3, 3, 59, tzinfo=timezone.utc)
        at_midnight = datetime(2026, 7, 3, 4, 0, tzinfo=timezone.utc)
        self.assertEqual(session_access(session, before), "NOT_YET_ACCESSIBLE_ON_BASIC")
        self.assertEqual(session_access(session, at_midnight), "ACCESSIBLE")

    def test_weekend_is_not_a_session(self):
        session = parse_iso_date("2026-11-07")
        now = datetime(2026, 11, 9, 15, 0, tzinfo=timezone.utc)
        self.assertEqual(session_access(session, now), "NOT_A_WEEKDAY_SESSION")

    def test_current_weekday_is_not_available_yet(self):
        session = parse_iso_date("2026-11-05")
        now = datetime(2026, 11, 5, 15, 0, tzinfo=timezone.utc)
        self.assertEqual(session_access(session, now), "NOT_YET_ACCESSIBLE_ON_BASIC")

    def test_naive_clock_is_rejected(self):
        with self.assertRaises(ValueError):
            session_access(parse_iso_date("2026-11-04"), datetime(2026, 11, 5, 12, 0))

    def test_history_window_matches_published_two_year_guard(self):
        session = parse_iso_date("2026-11-04")
        self.assertTrue(history_window_ok(parse_iso_date("2025-08-01"), session))
        self.assertFalse(history_window_ok(parse_iso_date("2024-01-01"), session))
        self.assertFalse(history_window_ok(session, session))


if __name__ == "__main__":
    unittest.main()
