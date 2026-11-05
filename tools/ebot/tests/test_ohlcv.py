"""Bar checks keep prices out of the summary."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401

from bars import SENTINEL_PRICE, SENTINEL_VOLUME, series
from ebot.ohlcv import summarise_bars
from ebot.report import format_report
from ebot.massive import new_report
from datetime import datetime, timezone


class OhlcvTests(unittest.TestCase):
    def test_260_weekday_bars_pass_without_echoing_prices(self):
        summary = summarise_bars(series("2026-11-04", 260))
        self.assertEqual(summary["coverage_260"], "PASS")
        self.assertEqual(summary["unique_sessions"], 260)
        self.assertEqual(summary["duplicate_records"], 0)
        self.assertEqual(summary["invalid_records"], 0)
        self.assertEqual(summary["latest"], "2026-11-04")
        self.assertEqual(summary["possible_missing_weekdays"], 0)
        self.assertNotIn("results", summary)
        blob = repr(summary)
        self.assertNotIn(str(SENTINEL_PRICE), blob)
        self.assertNotIn(str(SENTINEL_VOLUME), blob)

    def test_259_bars_hold(self):
        summary = summarise_bars(series("2026-11-04", 259))
        self.assertEqual(summary["coverage_260"], "HOLD")
        self.assertEqual(summary["unique_sessions"], 259)

    def test_duplicate_malformed_and_gap_are_counted_not_printed(self):
        bars = series("2026-11-04", 264)
        bars[10]["h"] = bars[10]["l"] - 1
        bars.append(dict(bars[-1]))
        del bars[20:24]
        summary = summarise_bars(bars)
        self.assertGreaterEqual(summary["invalid_records"], 1)
        self.assertGreaterEqual(summary["duplicate_records"], 1)
        self.assertEqual(summary["long_weekday_gap"], "yes")
        self.assertEqual(summary["coverage_260"], "HOLD")
        self.assertNotIn(str(SENTINEL_PRICE), repr(summary))

    def test_unordered_bars_hold(self):
        bars = series("2026-11-04", 260)
        bars[0], bars[1] = bars[1], bars[0]
        summary = summarise_bars(bars)
        self.assertEqual(summary["ordered"], "no")
        self.assertEqual(summary["coverage_260"], "HOLD")

    def test_non_list_payload_is_invalid(self):
        summary = summarise_bars({"t": 1})
        self.assertEqual(summary["coverage_260"], "HOLD")
        self.assertEqual(summary["invalid_records"], 1)

    def test_report_redacts_a_secret_that_reached_a_field(self):
        secret = "unit-test-massive-key"
        report = new_report("2026-11-04", "2025-08-01", datetime(2026, 11, 5, 15, tzinfo=timezone.utc))
        report["stopped_reason"] = "leaked " + secret + " apiKey=" + secret
        text = format_report(report, [secret])
        self.assertNotIn(secret, text)
        self.assertIn("[REDACTED]", text)
        self.assertIn("apiKey=[REDACTED]", text)
        self.assertIn("SECOND_SOURCE_NOT_TESTED", text)


if __name__ == "__main__":
    unittest.main()
