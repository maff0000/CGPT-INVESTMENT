"""Read-only Massive REST calls for the one allowlisted smoke test.

Endpoints match research/validation/g0_massive_readonly_probe.py:
one grouped US daily request and four ticker ranges. At most five GETs.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from typing import Callable, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ebot.calendar_rules import history_window_ok, session_access
from ebot.errors import (
    LocalCallCap,
    ProviderHttpError,
    ProviderPayloadError,
    ProviderTransportError,
)
from ebot.ohlcv import bar_is_invalid, summarise_bars

HOST = "https://api.massive.com"
SYMBOLS = ("XOM", "LIN", "EQIX", "SPY")
MAX_CALLS = 5
TIMEOUT_SECONDS = 35
MAX_BODY_BYTES = 32 * 1024 * 1024
DEFAULT_SESSION = "2026-11-04"
DEFAULT_FROM_DATE = "2025-08-01"

Send = Callable[[str], dict]


def grouped_path(session: str) -> str:
    _require_date(session)
    return "/v2/aggs/grouped/locale/us/market/stocks/" + session + "?adjusted=true"


def ticker_path(symbol: str, from_date: str, session: str) -> str:
    if symbol not in SYMBOLS:
        raise ValueError("symbol is not allowlisted")
    _require_date(from_date)
    _require_date(session)
    return (
        "/v2/aggs/ticker/" + symbol + "/range/1/day/"
        + from_date + "/" + session
        + "?adjusted=true&sort=asc&limit=5000"
    )


def _require_date(value: str) -> None:
    if len(value) != 10:
        raise ValueError("date")
    datetime.strptime(value, "%Y-%m-%d")


def public_status(value: object) -> str:
    """Keep short provider status tokens. Withhold free-text messages."""
    if not isinstance(value, str) or not value:
        return "NOT_RETURNED"
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    if 1 <= len(value) <= 32 and all(char in allowed for char in value):
        return value
    return "UNEXPECTED_STATUS_WITHHELD"


def adjustment_token(value: object) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "NOT_RETURNED"


def _count(value: object) -> str:
    if isinstance(value, bool) or not isinstance(value, int):
        return "WITHHELD"
    return str(value)


class Budget:
    """Count attempts and refuse a sixth call. Never retries."""

    def __init__(self, send: Send) -> None:
        self._send = send
        self.paths: list[str] = []
        self.stopped: Optional[str] = None

    def __call__(self, path: str) -> dict:
        if len(self.paths) >= MAX_CALLS:
            self.stopped = "LOCAL_CALL_CAP"
            raise LocalCallCap()
        if not path.startswith("/v2/"):
            raise ProviderPayloadError("REFUSING_PATH")
        self.paths.append(path)
        return self._send(path)


def urllib_send(api_key: str, opener=urlopen) -> Send:
    """HTTPS GET with a bearer header. The key is not placed in the URL."""

    def send(path: str) -> dict:
        if not path.startswith("/"):
            raise ProviderPayloadError("REFUSING_PATH")
        lowered = path.lower()
        if "apikey=" in lowered or (api_key and api_key in path):
            raise ProviderPayloadError("REFUSING_KEY_IN_URL")
        url = HOST + path
        if not url.startswith("https://api.massive.com/"):
            raise ProviderPayloadError("REFUSING_URL")
        request = Request(url, method="GET")
        request.add_header("Accept", "application/json")
        request.add_header("Authorization", "Bearer " + api_key)
        try:
            with opener(request, timeout=TIMEOUT_SECONDS) as response:
                raw = response.read(MAX_BODY_BYTES + 1)
                headers = getattr(response, "headers", None)
                charset = "utf-8"
                if headers is not None and hasattr(headers, "get_content_charset"):
                    charset = headers.get_content_charset() or "utf-8"
        except HTTPError as exc:
            raise ProviderHttpError(getattr(exc, "code", 0) or 0) from None
        except (URLError, TimeoutError, OSError):
            raise ProviderTransportError("TRANSPORT") from None
        if len(raw) > MAX_BODY_BYTES:
            raise ProviderPayloadError("RESPONSE_TOO_LARGE")
        try:
            payload = json.loads(raw.decode(charset))
        except (UnicodeError, json.JSONDecodeError):
            raise ProviderPayloadError("MALFORMED_JSON") from None
        if not isinstance(payload, dict):
            raise ProviderPayloadError("JSON_NOT_OBJECT")
        return payload

    return send


def _blank_symbol(symbol: str) -> dict:
    return {
        "symbol": symbol,
        "ran": False,
        "provider_status": "NOT_RUN",
        "daily_records": "NOT_RUN",
        "unique_sessions": "NOT_RUN",
        "earliest": "NOT_RUN",
        "latest": "NOT_RUN",
        "duplicate_records": "NOT_RUN",
        "invalid_records": "NOT_RUN",
        "ordered": "NOT_RUN",
        "possible_missing_weekdays": "NOT_RUN",
        "possible_missing_weekday_dates": [],
        "long_weekday_gap": "NOT_RUN",
        "coverage_260": "NOT_RUN",
        "ticker_identity": "NOT_RUN",
        "adjusted": "NOT_RUN",
        "results_count": "NOT_RUN",
        "issues": [],
    }


def new_report(session: str, from_date: str, now: datetime) -> dict:
    stamp = now.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "run_timestamp_utc": stamp,
        "requested_us_session": session,
        "from_date": from_date,
        "massive_connectivity": "NOT_EXECUTED",
        "overall": "HOLD",
        "calls_completed": 0,
        "partial": False,
        "stopped_reason": None,
        "provider_errors": [],
        "request_paths": [],
        "local_block": None,
        "successful_http": False,
        "grouped": {
            "ran": False,
            "http": "NOT_RUN",
            "provider_status": "NOT_RUN",
            "results_count": "NOT_RUN",
            "symbols_present": [],
            "symbols_missing": list(SYMBOLS),
            "duplicate_symbols": [],
            "invalid_symbol_rows": "NOT_RUN",
            "adjusted": "NOT_RUN",
        },
        "symbols": {symbol: _blank_symbol(symbol) for symbol in SYMBOLS},
        "adjustment_verified": "NOT_RETURNED",
    }


def _fill_grouped(report: dict, payload: dict) -> None:
    grouped = report["grouped"]
    grouped["ran"] = True
    grouped["http"] = "200"
    grouped["provider_status"] = public_status(payload.get("status"))
    grouped["results_count"] = _count(payload.get("resultsCount"))
    grouped["adjusted"] = adjustment_token(payload.get("adjusted"))
    present = []
    duplicates = []
    seen = set()
    invalid_rows = 0
    results = payload.get("results")
    if isinstance(results, list):
        for row in results:
            if not isinstance(row, dict):
                continue
            ticker = row.get("T")
            if ticker not in SYMBOLS:
                continue
            if bar_is_invalid(row):
                invalid_rows += 1
            if ticker in seen:
                duplicates.append(ticker)
            else:
                seen.add(ticker)
                present.append(ticker)
        grouped["invalid_symbol_rows"] = invalid_rows
    else:
        grouped["invalid_symbol_rows"] = "WITHHELD"
    grouped["symbols_present"] = [symbol for symbol in SYMBOLS if symbol in seen]
    grouped["symbols_missing"] = [symbol for symbol in SYMBOLS if symbol not in seen]
    grouped["duplicate_symbols"] = duplicates
    _note_adjustment(report, grouped["adjusted"])


def _fill_symbol(report: dict, symbol: str, payload: dict, session: str) -> None:
    row = report["symbols"][symbol]
    row["ran"] = True
    row["provider_status"] = public_status(payload.get("status"))
    row["adjusted"] = adjustment_token(payload.get("adjusted"))
    row["results_count"] = _count(payload.get("resultsCount"))
    identity = payload.get("ticker")
    row["ticker_identity"] = "PASS" if identity == symbol else "FAIL"
    summary = summarise_bars(payload.get("results"))
    for key in (
        "daily_records",
        "unique_sessions",
        "earliest",
        "latest",
        "duplicate_records",
        "invalid_records",
        "ordered",
        "possible_missing_weekdays",
        "possible_missing_weekday_dates",
        "long_weekday_gap",
        "coverage_260",
    ):
        row[key] = summary[key]
    issues = []
    if row["ticker_identity"] != "PASS":
        issues.append("TICKER_IDENTITY")
    if row["provider_status"] != "OK":
        issues.append("PROVIDER_STATUS")
    if row["latest"] != session:
        issues.append("LATEST_SESSION_IS_NOT_REQUESTED_SESSION")
    if row["coverage_260"] != "PASS":
        issues.append("COVERAGE")
    if isinstance(row["earliest"], str) and row["earliest"] not in {"NONE", "NOT_RUN"}:
        if row["earliest"] < report["from_date"]:
            issues.append("BAR_BEFORE_REQUESTED_WINDOW")
    row["issues"] = issues
    _note_adjustment(report, row["adjusted"])


def _note_adjustment(report: dict, token: str) -> None:
    current = report["adjustment_verified"]
    if token == "NOT_RETURNED":
        return
    if current in {"NOT_RETURNED", "NOT_RUN"}:
        report["adjustment_verified"] = token
    elif current != token:
        report["adjustment_verified"] = "MIXED"


def _coverage_pass(row: dict, session: str) -> bool:
    return (
        row["ran"]
        and row["provider_status"] == "OK"
        and row["ticker_identity"] == "PASS"
        and row["coverage_260"] == "PASS"
        and row["latest"] == session
        and row["adjusted"] != "false"
        and "BAR_BEFORE_REQUESTED_WINDOW" not in row["issues"]
    )


def judge(report: dict) -> None:
    """Set connectivity and overall. Never turns an unrun test into PASS."""
    if report["overall"] == "SETUP_NEEDED":
        report["massive_connectivity"] = "NOT_EXECUTED"
        return
    if report["local_block"]:
        report["massive_connectivity"] = "NOT_EXECUTED"
        report["overall"] = "HOLD"
        return
    if report["successful_http"]:
        report["massive_connectivity"] = "PASS"
    elif report["provider_errors"] and all(
        code in {"HTTP_403", "HTTP_429"} for code in report["provider_errors"]
    ):
        report["massive_connectivity"] = "HOLD"
    elif report["calls_completed"] == 0:
        report["massive_connectivity"] = "NOT_EXECUTED"
    else:
        report["massive_connectivity"] = "FAIL"

    grouped = report["grouped"]
    symbols_ok = all(
        _coverage_pass(report["symbols"][symbol], report["requested_us_session"])
        for symbol in SYMBOLS
    )
    full = (
        report["massive_connectivity"] == "PASS"
        and report["calls_completed"] == MAX_CALLS
        and not report["stopped_reason"]
        and not report["provider_errors"]
        and grouped["ran"]
        and grouped["provider_status"] == "OK"
        and not grouped["symbols_missing"]
        and not grouped["duplicate_symbols"]
        and grouped["adjusted"] != "false"
        and grouped["invalid_symbol_rows"] == 0
        and symbols_ok
        and report["adjustment_verified"] != "false"
        and report["adjustment_verified"] != "MIXED"
    )
    if full:
        report["overall"] = "PASS"
    elif report["massive_connectivity"] == "FAIL":
        report["overall"] = "FAIL"
    else:
        report["overall"] = "HOLD"


def parse_iso_date(value: str) -> date:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValueError("date") from None
    return parsed.date()


def preflight(session: str, from_date: str, now: datetime) -> Optional[dict]:
    """Return a finished report when the run must stop before any key or HTTP use."""
    report = new_report(session, from_date, now)
    try:
        session_date = parse_iso_date(session)
        start_date = parse_iso_date(from_date)
    except ValueError:
        report["local_block"] = "INVALID_DATE"
        judge(report)
        return report
    if start_date >= session_date:
        report["local_block"] = "FROM_DATE_NOT_BEFORE_SESSION"
        judge(report)
        return report
    access = session_access(session_date, now)
    if access != "ACCESSIBLE":
        report["local_block"] = access
        judge(report)
        return report
    if not history_window_ok(start_date, session_date):
        report["local_block"] = "BASIC_HISTORY_WINDOW"
        judge(report)
        return report
    return None


def run_smoke(
    session: str,
    from_date: str,
    api_key: Optional[str],
    *,
    now: datetime,
    transport_factory: Optional[Callable[[str], Send]] = None,
) -> dict:
    """Run the allowlisted check, or stop locally before any HTTP call."""
    blocked = preflight(session, from_date, now)
    if blocked is not None:
        return blocked
    report = new_report(session, from_date, now)
    if not api_key:
        report["overall"] = "SETUP_NEEDED"
        judge(report)
        return report

    factory = transport_factory or urllib_send
    budget = Budget(factory(api_key))
    try:
        grouped_payload = budget(grouped_path(session))
        report["successful_http"] = True
        _fill_grouped(report, grouped_payload)
        if report["grouped"]["provider_status"] != "OK":
            report["stopped_reason"] = "GROUPED_STATUS_" + report["grouped"]["provider_status"]
        else:
            for symbol in SYMBOLS:
                payload = budget(ticker_path(symbol, from_date, session))
                report["successful_http"] = True
                _fill_symbol(report, symbol, payload, session)
                if report["symbols"][symbol]["provider_status"] != "OK":
                    report["stopped_reason"] = "TICKER_STATUS_" + symbol
                    break
    except ProviderHttpError as exc:
        report["provider_errors"].append("HTTP_" + str(exc.code))
        report["stopped_reason"] = "HTTP_" + str(exc.code) + "_NO_RETRY"
    except ProviderPayloadError as exc:
        report["provider_errors"].append(str(exc) or "PAYLOAD")
        report["stopped_reason"] = "PAYLOAD_NO_RETRY"
    except ProviderTransportError as exc:
        report["provider_errors"].append(str(exc) or "TRANSPORT")
        report["stopped_reason"] = "TRANSPORT_NO_RETRY"
    except LocalCallCap:
        report["stopped_reason"] = "LOCAL_CALL_CAP"
    report["calls_completed"] = len(budget.paths)
    report["request_paths"] = list(budget.paths)
    report["partial"] = report["stopped_reason"] is not None
    judge(report)
    return report
