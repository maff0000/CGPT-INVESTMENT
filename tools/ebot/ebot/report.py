"""Compact text report. No raw bars, no credentials, no second-source invention."""

from __future__ import annotations

from ebot.massive import SYMBOLS
from ebot.redact import redact

_STANDING = (
    "G0 remains OPEN. This run does not accept a canonical provider, a licence, "
    "Finviz A/B/C, a chart stage, or an investment.",
    "SECOND_SOURCE_NOT_TESTED. No close comparison was invented.",
    "Commercial redistribution rights for Massive data are not decided here.",
    "Exchange holidays are not in this tool. Weekday gaps are candidates only.",
    "Basic plan serves a completed session only after midnight America/New_York "
    "on the next calendar day. Do not rerun the five-call batch inside one minute.",
)


def _join(values: list[str]) -> str:
    return ",".join(values) if values else "none"


def format_report(report: dict, secrets: list[str]) -> str:
    lines = [
        "E-Bot v0.1 validation report",
        "tool: E-Bot",
        "version: 0.1.0",
        "run_timestamp_utc: " + report["run_timestamp_utc"],
        "requested_us_session: " + report["requested_us_session"],
        "from_date: " + report["from_date"],
        "session_clock: America/New_York",
        "bar_date_convention: UTC calendar date of the provider timestamp",
        "massive_connectivity: " + report["massive_connectivity"],
        "overall: " + report["overall"],
        "calls_completed: " + str(report["calls_completed"]),
        "call_cap: 5",
        "retries: 0",
        "partial: " + ("yes" if report["partial"] else "no"),
        "stopped_reason: " + (report["stopped_reason"] or "none"),
        "local_block: " + (report["local_block"] or "none"),
        "adjustment_convention: split-adjusted when adjusted=true; "
        "Massive documents that aggregates are not dividend-adjusted",
        "adjustment_payload_flag: " + report["adjustment_verified"],
        "price_comparison: SECOND_SOURCE_NOT_TESTED",
        "price_rule_retained: absolute USD close difference <= 1.00 PRICE_OK; "
        "> 1.00 PRICE_CHECK; pivot straddle SIGNAL_AMBIGUOUS; "
        "instrument, session, currency or adjustment mismatch DATA_MISMATCH",
        "g0_acceptance: OPEN",
        "finviz_abc: NOT_RUN",
        "chart_stage: NOT_RUN",
        "investment_decision: NOT_RUN",
        "pass_means: access and bar-count checks only, and only when overall is PASS",
    ]
    grouped = report["grouped"]
    lines.extend([
        "grouped_daily:",
        "  http: " + grouped["http"],
        "  provider_status: " + grouped["provider_status"],
        "  results_count: " + str(grouped["results_count"]),
        "  symbols_present: " + _join(grouped["symbols_present"]),
        "  symbols_missing: " + _join(grouped["symbols_missing"]),
        "  duplicate_symbols: " + _join(grouped["duplicate_symbols"]),
        "  invalid_symbol_rows: " + str(grouped["invalid_symbol_rows"]),
        "  adjusted: " + grouped["adjusted"],
    ])
    for symbol in SYMBOLS:
        row = report["symbols"][symbol]
        dates = row["possible_missing_weekday_dates"]
        lines.extend([
            "symbol: " + symbol,
            "  provider_status: " + str(row["provider_status"]),
            "  daily_records: " + str(row["daily_records"]),
            "  unique_sessions: " + str(row["unique_sessions"]),
            "  earliest: " + str(row["earliest"]),
            "  latest: " + str(row["latest"]),
            "  duplicate_records: " + str(row["duplicate_records"]),
            "  invalid_records: " + str(row["invalid_records"]),
            "  ordered: " + str(row["ordered"]),
            "  possible_missing_weekdays: " + str(row["possible_missing_weekdays"]),
            "  possible_missing_weekday_dates: " + _join(dates),
            "  long_weekday_gap: " + str(row["long_weekday_gap"]),
            "  coverage_260: " + str(row["coverage_260"]),
            "  ticker_identity: " + str(row["ticker_identity"]),
            "  adjusted: " + str(row["adjusted"]),
        ])
    errors = report["provider_errors"]
    lines.append("provider_errors: " + (_join(errors) if errors else "none"))
    if report["request_paths"]:
        lines.append("requests:")
        for path in report["request_paths"]:
            lines.append("- GET " + path)
    else:
        lines.append("requests: none")
    lines.append("outstanding_issues:")
    for item in _issues(report):
        lines.append("- " + item)
    text = "\n".join(lines) + "\n"
    return redact(text, secrets)


def _issues(report: dict) -> list[str]:
    items = []
    if report["overall"] == "SETUP_NEEDED":
        items.append(
            "SETUP_NEEDED. No Massive API key was available, so no request was sent."
        )
    if report["local_block"]:
        items.append("Local block before any request: " + report["local_block"] + ".")
    if report["massive_connectivity"] == "NOT_EXECUTED":
        items.append("Massive connectivity was not executed. It is not PASS.")
    if report["provider_errors"]:
        items.append("Provider or transport errors: " + ", ".join(report["provider_errors"]) + ".")
    if report["partial"]:
        items.append(
            "The five-call batch stopped early. It was not repeated. "
            "Wait at least one minute before a new manual run."
        )
    grouped = report["grouped"]
    if grouped["ran"] and grouped["symbols_missing"]:
        items.append(
            "Grouped daily response missed: " + ", ".join(grouped["symbols_missing"]) + "."
        )
    for symbol in SYMBOLS:
        row = report["symbols"][symbol]
        for issue in row["issues"]:
            items.append(symbol + " " + issue + ".")
    if report["overall"] == "PASS":
        items.append(
            "overall PASS covers this manual read-only check only. "
            "It does not close G0 or authorise an investment."
        )
    items.extend(_STANDING)
    return items
