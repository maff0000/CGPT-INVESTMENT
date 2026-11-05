"""Command line: help, prompt, run, secrets, and no network on rejection."""

from __future__ import annotations

import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401
import os
import tempfile
import unittest
from pathlib import Path

from bars import SENTINEL_PRICE, SENTINEL_VOLUME
from ebot.cli import main
from ebot.massive import SYMBOLS, grouped_path, ticker_path
from test_massive import FROM_DATE, KEY, NOW, SESSION, _factory

class Silent:
    def isatty(self):
        return False


class Tty:
    def isatty(self):
        return True


class CliTests(unittest.TestCase):
    def test_help_lists_the_only_task_and_the_restrictions(self):
        out = io.StringIO()
        code = main(["help"], stdout=out, stderr=io.StringIO())
        text = out.getvalue()
        self.assertEqual(code, 0)
        for snippet in (
            "E-Bot v0.1",
            "massive-smoke",
            "XOM",
            "LIN",
            "EQIX",
            "SPY",
            "read-only",
            "5",
            "SETUP_NEEDED",
            "PRICE_OK",
            "PRICE_CHECK",
            "SIGNAL_AMBIGUOUS",
            "shell",
            "broker",
            "Finviz",
            "G0",
            "api.massive.com",
        ):
            self.assertIn(snippet, text)

    def test_unsupported_prompt_makes_no_call(self):
        out = io.StringIO()
        code = main(
            ["prompt", "rm -rf /tmp/not-a-task"],
            transport_factory=lambda _key: (_ for _ in ()).throw(AssertionError("called")),
            prompter=lambda _prompt: (_ for _ in ()).throw(AssertionError("prompted")),
            now=NOW,
            stdin=Tty(),
            stdout=out,
            stderr=io.StringIO(),
        )
        self.assertEqual(code, 3)
        self.assertIn("result: REJECTED", out.getvalue())
        self.assertIn("UNSUPPORTED", out.getvalue())
        self.assertIn("request_sent: no", out.getvalue())

    def test_ambiguous_prompt_is_rejected(self):
        out = io.StringIO()
        code = main(
            ["prompt", "Check Massive connectivity and historical data availability for XOM, LIN, EQIX and SPY."],
            now=NOW,
            stdin=Silent(),
            stdout=out,
            stderr=io.StringIO(),
        )
        self.assertEqual(code, 3)
        self.assertIn("AMBIGUOUS", out.getvalue())
        self.assertIn("request_sent: no", out.getvalue())

    def test_allowlisted_prompt_prints_the_task_then_runs_it(self):
        calls = []
        out = io.StringIO()
        phrase = (
            "Check Massive connectivity and 260+ daily bars for "
            "XOM, LIN, EQIX, SPY as at 2026-11-04"
        )
        code = main(
            ["prompt", phrase, "--key-file", _key_file()],
            transport_factory=_factory(calls),
            now=NOW,
            stdin=Silent(),
            stdout=out,
            stderr=io.StringIO(),
        )
        text = out.getvalue()
        self.assertEqual(code, 0, text)
        self.assertLess(text.index("Interpreted task:"), text.index("validation report"))
        self.assertIn("--session 2026-11-04 --from-date 2025-08-01", text)
        self.assertEqual(len(calls), 5)
        self.assertNotIn(KEY, text)
        self.assertNotIn(str(SENTINEL_PRICE), text)
        self.assertNotIn(str(SENTINEL_VOLUME), text)

    def test_missing_key_is_setup_needed(self):
        out = io.StringIO()
        code = main(
            ["run", "massive-smoke", "--session", SESSION, "--from-date", FROM_DATE],
            transport_factory=lambda _key: (_ for _ in ()).throw(AssertionError("called")),
            prompter=lambda _prompt: (_ for _ in ()).throw(AssertionError("prompted")),
            now=NOW,
            stdin=Silent(),
            stdout=out,
            stderr=io.StringIO(),
        )
        text = out.getvalue()
        self.assertEqual(code, 2)
        self.assertIn("overall: SETUP_NEEDED", text)
        self.assertIn("massive_connectivity: NOT_EXECUTED", text)

    def test_credential_flag_is_refused_without_echoing_the_value(self):
        out = io.StringIO()
        err = io.StringIO()
        code = main(
            ["run", "massive-smoke", "--api-key", KEY],
            stdout=out,
            stderr=err,
        )
        combined = out.getvalue() + err.getvalue()
        self.assertEqual(code, 3)
        self.assertNotIn(KEY, combined)
        self.assertIn("Refusing a credential", combined)

    def test_unknown_task_is_rejected(self):
        out = io.StringIO()
        code = main(["run", "buy-stocks"], stdout=out, stderr=io.StringIO(), now=NOW)
        self.assertEqual(code, 3)
        self.assertIn("REJECTED", out.getvalue())

    def test_weekend_session_does_not_ask_for_a_key(self):
        out = io.StringIO()
        code = main(
            ["run", "massive-smoke", "--session", "2026-11-07", "--from-date", FROM_DATE],
            prompter=lambda _prompt: (_ for _ in ()).throw(AssertionError("prompted")),
            transport_factory=lambda _key: (_ for _ in ()).throw(AssertionError("called")),
            now=NOW,
            stdin=Tty(),
            stdout=out,
            stderr=io.StringIO(),
        )
        self.assertEqual(code, 4)
        self.assertIn("NOT_A_WEEKDAY_SESSION", out.getvalue())
        self.assertIn("requests: none", out.getvalue())

    def test_explicit_run_uses_five_get_paths(self):
        calls = []
        out = io.StringIO()
        code = main(
            ["run", "massive-smoke", "--session", SESSION, "--from-date", FROM_DATE, "--key-file", _key_file()],
            transport_factory=_factory(calls),
            now=NOW,
            stdin=Silent(),
            stdout=out,
            stderr=io.StringIO(),
        )
        self.assertEqual(code, 0, out.getvalue())
        self.assertEqual(calls[0], grouped_path(SESSION))
        self.assertEqual(calls[1:], [ticker_path(symbol, FROM_DATE, SESSION) for symbol in SYMBOLS])

    def test_transport_exception_text_cannot_leak_the_key(self):
        out = io.StringIO()
        err = io.StringIO()

        def build(api_key):
            def send(_path):
                raise RuntimeError("provider said " + api_key)

            return send

        code = main(
            ["run", "massive-smoke", "--session", SESSION, "--from-date", FROM_DATE],
            transport_factory=build,
            prompter=lambda _prompt: KEY,
            now=NOW,
            stdin=Tty(),
            stdout=out,
            stderr=err,
        )
        combined = out.getvalue() + err.getvalue()
        self.assertEqual(code, 1)
        self.assertNotIn(KEY, combined)
        self.assertIn("RuntimeError", combined)

    def test_world_readable_key_file_does_not_print_the_key(self):
        handle, name = tempfile.mkstemp(prefix="ebot-key-")
        os.close(handle)
        path = Path(name)
        try:
            path.write_text(KEY + "\n", encoding="utf-8")
            os.chmod(path, 0o644)
            out = io.StringIO()
            err = io.StringIO()
            code = main(
                ["run", "massive-smoke", "--session", SESSION, "--from-date", FROM_DATE, "--key-file", name],
                now=NOW,
                stdin=Silent(),
                stdout=out,
                stderr=err,
            )
            combined = out.getvalue() + err.getvalue()
            self.assertEqual(code, 2)
            self.assertNotIn(KEY, combined)
            self.assertIn("0600", combined)
        finally:
            path.unlink(missing_ok=True)


def _key_file():
    handle, name = tempfile.mkstemp(prefix="ebot-key-")
    os.close(handle)
    path = Path(name)
    path.write_text(KEY + "\n", encoding="utf-8")
    os.chmod(path, 0o600)
    return name


if __name__ == "__main__":
    unittest.main()
