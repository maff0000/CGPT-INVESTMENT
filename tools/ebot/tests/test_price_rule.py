"""G0-DATA-002 boundaries. No vendor feed is consulted."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401

from ebot.price_rule import DATA_MISMATCH, PRICE_CHECK, PRICE_OK, SIGNAL_AMBIGUOUS, compare_closes


def _same(**overrides):
    base = dict(
        instrument_a="XOM",
        instrument_b="XOM",
        session_a="2026-11-04",
        session_b="2026-11-04",
        currency_a="USD",
        currency_b="USD",
        adjustment_a="split-adjusted",
        adjustment_b="split-adjusted",
        pivot=None,
    )
    base.update(overrides)
    return base


class PriceRuleTests(unittest.TestCase):
    def test_one_dollar_is_price_ok(self):
        result = compare_closes("100.00", "101.00", **_same())
        self.assertEqual(result["state"], PRICE_OK)
        self.assertIsNone(result["signal"])
        self.assertEqual(result["absolute_difference"], "1.00")

    def test_one_cent_over_is_price_check(self):
        result = compare_closes("100.00", "101.01", **_same())
        self.assertEqual(result["state"], PRICE_CHECK)
        self.assertEqual(result["absolute_difference"], "1.01")

    def test_documented_table(self):
        self.assertEqual(compare_closes("100.00", "100.99", **_same())["state"], PRICE_OK)
        self.assertEqual(compare_closes("100.00", "101.00", **_same())["state"], PRICE_OK)
        self.assertEqual(compare_closes("100.00", "101.01", **_same())["state"], PRICE_CHECK)

    def test_pivot_straddle_blocks_breakout_without_price_check(self):
        result = compare_closes("100.20", "100.70", **_same(pivot="100.50"))
        self.assertEqual(result["state"], PRICE_OK)
        self.assertEqual(result["signal"], SIGNAL_AMBIGUOUS)
        self.assertEqual(result["breakout_confirmation"], "BLOCKED")

    def test_same_side_of_pivot_does_not_confirm_a_breakout(self):
        result = compare_closes("100.60", "100.80", **_same(pivot="100.50"))
        self.assertEqual(result["state"], PRICE_OK)
        self.assertIsNone(result["signal"])
        self.assertEqual(result["breakout_confirmation"], "NOT_BLOCKED_BY_PIVOT_STRADDLE")

    def test_session_mismatch_does_not_apply_the_dollar_rule(self):
        result = compare_closes("100.00", "100.20", **_same(session_b="2026-11-03"))
        self.assertEqual(result["state"], DATA_MISMATCH)
        self.assertIsNone(result["absolute_difference"])
        self.assertEqual(result["breakout_confirmation"], "BLOCKED")

    def test_adjustment_mismatch_is_data_mismatch(self):
        result = compare_closes(
            "25",
            "12.50",
            **_same(adjustment_a="raw", adjustment_b="split-adjusted"),
        )
        self.assertEqual(result["state"], DATA_MISMATCH)
        self.assertNotEqual(result["state"], PRICE_CHECK)

    def test_currency_or_instrument_mismatch(self):
        self.assertEqual(
            compare_closes("10", "10", **_same(currency_b="EUR"))["state"],
            DATA_MISMATCH,
        )
        self.assertEqual(
            compare_closes("10", "11.50", **_same(instrument_b="LIN"))["state"],
            DATA_MISMATCH,
        )


if __name__ == "__main__":
    unittest.main()
