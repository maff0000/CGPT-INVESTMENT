"""Massive smoke behaviour with a fake transport. No live API."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402,F401
import unittest
from datetime import datetime, timezone
from urllib.error import HTTPError

from bars import SENTINEL_PRICE, SENTINEL_VOLUME, bar, series
from ebot.errors import LocalCallCap, ProviderHttpError, ProviderPayloadError
from ebot.massive import (
    SYMBOLS,
    Budget,
    grouped_path,
    run_smoke,
    ticker_path,
    urllib_send,
)
from ebot.report import format_report

SESSION = "2026-11-04"
FROM_DATE = "2025-08-01"
NOW = datetime(2026, 11, 5, 15, 0, tzinfo=timezone.utc)
KEY = "unit-test-massive-key"


def _grouped(session=SESSION):
    day_bar = bar(datetime.strptime(session, "%Y-%m-%d").date())
    rows = []
    for symbol in SYMBOLS:
        row = dict(day_bar)
        row["T"] = symbol
        rows.append(row)
    return {"status": "OK", "adjusted": True, "resultsCount": len(rows), "results": rows}


def _ticker(symbol, session=SESSION, count=260):
    bars = series(session, count)
    return {
        "ticker": symbol,
        "status": "OK",
        "adjusted": True,
        "resultsCount": len(bars),
        "results": bars,
    }


def _factory(calls, ticker_count=260, grouped_status="OK", ticker_status="OK"):
    def build(api_key):
        def send(path):
            if api_key in path or "apiKey=" in path:
                raise AssertionError("credential reached the URL")
            calls.append(path)
            if "/grouped/" in path:
                payload = _grouped()
                payload["status"] = grouped_status
                return payload
            for symbol in SYMBOLS:
                marker = "/ticker/" + symbol + "/"
                if marker in path:
                    payload = _ticker(symbol, count=ticker_count)
                    payload["status"] = ticker_status
                    return payload
            raise AssertionError(path)

        return send

    return build


class PathTests(unittest.TestCase):
    def test_paths_match_the_existing_probe(self):
        self.assertEqual(
            grouped_path(SESSION),
            "/v2/aggs/grouped/locale/us/market/stocks/2026-11-04?adjusted=true",
        )
        self.assertEqual(
            ticker_path("XOM", FROM_DATE, SESSION),
            "/v2/aggs/ticker/XOM/range/1/day/2025-08-01/2026-11-04?adjusted=true&sort=asc&limit=5000",
        )

    def test_symbol_outside_the_allowlist_cannot_build_a_url(self):
        with self.assertRaises(ValueError):
            ticker_path("AAPL", FROM_DATE, SESSION)


class BudgetTests(unittest.TestCase):
    def test_sixth_call_is_not_sent(self):
        sent = []

        def send(path):
            sent.append(path)
            return {"status": "OK"}

        budget = Budget(send)
        for _ in range(5):
            budget("/v2/ok")
        with self.assertRaises(LocalCallCap):
            budget("/v2/sixth")
        self.assertEqual(sent, ["/v2/ok"] * 5)
        self.assertNotIn("/v2/sixth", budget.paths)


class SmokeTests(unittest.TestCase):
    def test_full_success_is_pass_without_prices_or_a_second_source(self):
        calls = []
        report = run_smoke(
            SESSION,
            FROM_DATE,
            KEY,
            now=NOW,
            transport_factory=_factory(calls),
        )
        text = format_report(report, [KEY])
        self.assertEqual(report["overall"], "PASS")
        self.assertEqual(report["massive_connectivity"], "PASS")
        self.assertEqual(report["calls_completed"], 5)
        self.assertEqual(len(calls), 5)
        self.assertIn("/grouped/", calls[0])
        self.assertEqual(
            [path for path in calls if "/ticker/" in path],
            [ticker_path(symbol, FROM_DATE, SESSION) for symbol in SYMBOLS],
        )
        for symbol in SYMBOLS:
            self.assertEqual(report["symbols"][symbol]["daily_records"], 260)
            self.assertEqual(report["symbols"][symbol]["latest"], SESSION)
            self.assertNotEqual(report["symbols"][symbol]["earliest"], "NOT_RUN")
        self.assertIn("price_comparison: SECOND_SOURCE_NOT_TESTED", text)
        self.assertIn("g0_acceptance: OPEN", text)
        self.assertIn("adjustment_convention: split-adjusted", text)
        self.assertNotIn(str(SENTINEL_PRICE), text)
        self.assertNotIn(str(SENTINEL_VOLUME), text)
        self.assertNotIn(KEY, text)
        self.assertNotIn("absolute_difference:", text)

    def test_short_history_holds_and_does_not_claim_pass(self):
        calls = []
        report = run_smoke(
            SESSION,
            FROM_DATE,
            KEY,
            now=NOW,
            transport_factory=_factory(calls, ticker_count=259),
        )
        self.assertEqual(report["massive_connectivity"], "PASS")
        self.assertEqual(report["overall"], "HOLD")
        self.assertEqual(report["symbols"]["XOM"]["coverage_260"], "HOLD")
        self.assertEqual(len(calls), 5)

    def test_missing_key_does_not_call_transport(self):
        def build(_key):
            raise AssertionError("transport built")

        report = run_smoke(SESSION, FROM_DATE, None, now=NOW, transport_factory=build)
        text = format_report(report, [])
        self.assertEqual(report["overall"], "SETUP_NEEDED")
        self.assertEqual(report["massive_connectivity"], "NOT_EXECUTED")
        self.assertIn("requests: none", text)
        self.assertNotIn("massive_connectivity: PASS", text)

    def test_calendar_block_does_not_call_transport(self):
        def build(_key):
            raise AssertionError("transport built")

        early = datetime(2026, 11, 5, 4, 30, tzinfo=timezone.utc)
        report = run_smoke(SESSION, FROM_DATE, KEY, now=early, transport_factory=build)
        self.assertEqual(report["local_block"], "NOT_YET_ACCESSIBLE_ON_BASIC")
        self.assertEqual(report["overall"], "HOLD")
        self.assertEqual(report["calls_completed"], 0)

    def test_history_window_blocks_before_http(self):
        def build(_key):
            raise AssertionError("transport built")

        report = run_smoke(
            SESSION,
            "2024-01-01",
            KEY,
            now=NOW,
            transport_factory=build,
        )
        self.assertEqual(report["local_block"], "BASIC_HISTORY_WINDOW")
        self.assertEqual(report["massive_connectivity"], "NOT_EXECUTED")

    def test_401_fails_without_retry(self):
        calls = []

        def build(_key):
            def send(path):
                calls.append(path)
                raise ProviderHttpError(401)

            return send

        report = run_smoke(SESSION, FROM_DATE, KEY, now=NOW, transport_factory=build)
        self.assertEqual(calls, [grouped_path(SESSION)])
        self.assertEqual(report["overall"], "FAIL")
        self.assertEqual(report["massive_connectivity"], "FAIL")
        self.assertEqual(report["stopped_reason"], "HTTP_401_NO_RETRY")
        self.assertEqual(report["symbols"]["LIN"]["coverage_260"], "NOT_RUN")

    def test_403_and_429_hold_and_do_not_loop(self):
        for code, expected_connectivity in ((403, "HOLD"), (429, "PASS")):
            calls = []

            def build(_key, status_code=code):
                def send(path):
                    calls.append(path)
                    if status_code == 429 and len(calls) == 1:
                        return _grouped()
                    raise ProviderHttpError(status_code)

                return send

            report = run_smoke(SESSION, FROM_DATE, KEY, now=NOW, transport_factory=build)
            self.assertLessEqual(len(calls), 2)
            self.assertEqual(len(calls), len(set(calls)))
            self.assertEqual(report["massive_connectivity"], expected_connectivity)
            self.assertEqual(report["overall"], "HOLD")
            self.assertIn("NO_RETRY", report["stopped_reason"])

    def test_malformed_payload_fails_without_saving_a_body(self):
        def build(_key):
            def send(_path):
                raise ProviderPayloadError("MALFORMED_JSON")

            return send

        report = run_smoke(SESSION, FROM_DATE, KEY, now=NOW, transport_factory=build)
        text = format_report(report, [KEY])
        self.assertEqual(report["overall"], "FAIL")
        self.assertIn("MALFORMED_JSON", text)
        self.assertNotIn(str(SENTINEL_PRICE), text)

    def test_grouped_symbol_gap_holds_even_when_history_is_complete(self):
        def build(_key):
            def send(path):
                if "/grouped/" in path:
                    payload = _grouped()
                    payload["results"] = [row for row in payload["results"] if row["T"] != "EQIX"]
                    return payload
                for symbol in SYMBOLS:
                    if "/ticker/" + symbol + "/" in path:
                        return _ticker(symbol)
                raise AssertionError(path)

            return send

        report = run_smoke(SESSION, FROM_DATE, KEY, now=NOW, transport_factory=build)
        self.assertEqual(report["overall"], "HOLD")
        self.assertEqual(report["grouped"]["symbols_missing"], ["EQIX"])
        self.assertEqual(report["symbols"]["EQIX"]["coverage_260"], "PASS")

    def test_provider_status_text_is_withheld(self):
        calls = []

        def build(api_key):
            def send(path):
                calls.append(path)
                payload = _grouped()
                payload["status"] = "error near " + api_key
                return payload

            return send

        report = run_smoke(SESSION, FROM_DATE, KEY, now=NOW, transport_factory=build)
        text = format_report(report, [KEY])
        self.assertEqual(len(calls), 1)
        self.assertEqual(report["grouped"]["provider_status"], "UNEXPECTED_STATUS_WITHHELD")
        self.assertNotIn(KEY, text)
        self.assertEqual(report["overall"], "HOLD")


class UrllibSendTests(unittest.TestCase):
    def test_request_is_https_get_with_bearer_header_and_timeout(self):
        captured = {}

        class Headers:
            def get_content_charset(self, failobj=None):
                return "utf-8"

        class Response:
            headers = Headers()

            def read(self, _limit=-1):
                return b'{"status": "OK", "results": []}'

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        def opener(request, timeout=0):
            captured["url"] = request.full_url
            captured["method"] = request.get_method()
            captured["timeout"] = timeout
            captured["auth"] = request.get_header("Authorization")
            return Response()

        payload = urllib_send(KEY, opener=opener)(grouped_path(SESSION))
        self.assertEqual(payload["status"], "OK")
        self.assertTrue(captured["url"].startswith("https://api.massive.com/"))
        self.assertNotIn(KEY, captured["url"])
        self.assertNotIn("apiKey", captured["url"])
        self.assertEqual(captured["method"], "GET")
        self.assertEqual(captured["timeout"], 35)
        self.assertEqual(captured["auth"], "Bearer " + KEY)

    def test_http_error_keeps_only_the_status_code(self):
        def opener(request, timeout=0):
            raise HTTPError(request.full_url, 401, "secret " + KEY, None, None)

        send = urllib_send(KEY, opener=opener)
        with self.assertRaises(ProviderHttpError) as caught:
            send(grouped_path(SESSION))
        self.assertEqual(caught.exception.code, 401)
        self.assertNotIn(KEY, str(caught.exception))

    def test_malformed_json_does_not_return_the_body(self):
        class Headers:
            def get_content_charset(self, failobj=None):
                return "utf-8"

        class Response:
            headers = Headers()

            def read(self, _limit=-1):
                return b"not-json " + KEY.encode("ascii")

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        send = urllib_send(KEY, opener=lambda request, timeout=0: Response())
        with self.assertRaises(ProviderPayloadError) as caught:
            send(grouped_path(SESSION))
        self.assertEqual(str(caught.exception), "MALFORMED_JSON")
        self.assertNotIn(KEY, str(caught.exception))
        self.assertNotIn("not-json", str(caught.exception))

    def test_non_object_json_is_rejected(self):
        class Headers:
            def get_content_charset(self, failobj=None):
                return "utf-8"

        class Response:
            headers = Headers()

            def read(self, _limit=-1):
                return json.dumps([SENTINEL_PRICE]).encode("ascii")

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        send = urllib_send(KEY, opener=lambda request, timeout=0: Response())
        with self.assertRaises(ProviderPayloadError) as caught:
            send(grouped_path(SESSION))
        self.assertEqual(str(caught.exception), "JSON_NOT_OBJECT")


if __name__ == "__main__":
    unittest.main()
