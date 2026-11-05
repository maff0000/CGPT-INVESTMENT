"""Deterministic allowlist for E-Bot prompts.

Free text never becomes a shell command, a URL, a path, or an API query.
"""

from __future__ import annotations

import re
from datetime import datetime

DEFAULT_FROM_DATE = "2025-08-01"
ACCEPTED_PROMPT = (
    "Check Massive connectivity and 260+ daily bars for "
    "XOM, LIN, EQIX, SPY as at YYYY-MM-DD"
)

_DATE = r"(\d{4}-\d{2}-\d{2})"
_ALLOWLIST = re.compile(
    r"^check massive connectivity and 260\+ daily bars for "
    r"xom, lin, eqix(?:,| and) spy as (?:at|of) " + _DATE + r"$"
)
_UNDATED = {
    "check massive connectivity and historical data availability for xom, lin, eqix and spy",
    "check massive connectivity and historical data availability for xom, lin, eqix, spy",
}
_META = re.compile(r"[;&|$<>`\"'\\(){}\[\]]|://|\.\./")
_KEYWORDS = re.compile(
    r"\b(sudo|curl|wget|rm|python|bash|eval|exec|subprocess|os\.system)\b"
)


def normalise(text: str) -> str:
    cleaned = text.strip().lower().replace("260 +", "260+")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.rstrip(".")


def _valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def parse_prompt(text: str) -> dict:
    """Map one instruction onto massive-smoke, or reject it.

    Accepted prompts use the fixed symbols and default from-date
    ``2025-08-01``. The operator sees that interpretation before any call.
    """
    if text is None or not str(text).strip():
        return _reject("EMPTY", "The instruction was empty. No request was sent.")
    raw = str(text)
    if len(raw) > 500 or _META.search(raw) or _KEYWORDS.search(raw.lower()):
        return _reject(
            "UNSUPPORTED",
            "The instruction is not an allowlisted data check. "
            "E-Bot does not run shell commands, arbitrary code, URLs or file paths. "
            "No request was sent.",
        )
    normalised = normalise(raw)
    match = _ALLOWLIST.match(normalised)
    if match:
        session = match.group(1)
        if not _valid_date(session):
            return _reject(
                "INVALID_DATE",
                "The session date is not a real calendar date. No request was sent.",
            )
        return {
            "accepted": True,
            "reason": "ALLOWLISTED",
            "task": "massive-smoke",
            "session": session,
            "from_date": DEFAULT_FROM_DATE,
            "detail": (
                "Interpreted task: ebot run massive-smoke --session {session} "
                "--from-date {from_date}. Symbols are fixed: XOM, LIN, EQIX, SPY. "
                "No other instruction will be executed."
            ).format(session=session, from_date=DEFAULT_FROM_DATE),
        }
    if normalised in _UNDATED:
        return _reject(
            "AMBIGUOUS",
            "The instruction names the Massive coverage check but does not give "
            "one completed US session date. Restate it with 'as at YYYY-MM-DD'. "
            "No request was sent.",
        )
    return _reject(
        "UNRECOGNISED",
        "The instruction is not an allowlisted E-Bot task. "
        "No shell command, URL, file or API request was run.",
    )


def _reject(reason: str, detail: str) -> dict:
    return {
        "accepted": False,
        "reason": reason,
        "task": None,
        "session": None,
        "from_date": None,
        "detail": detail,
    }


def format_rejection(parsed: dict) -> str:
    lines = [
        "E-Bot v0.1",
        "result: REJECTED",
        "reason: " + parsed["reason"],
        "request_sent: no",
        "detail: " + parsed["detail"],
        "allowlisted_prompt: " + ACCEPTED_PROMPT,
        "allowlisted_command: ebot run massive-smoke --session YYYY-MM-DD "
        "--from-date YYYY-MM-DD",
    ]
    return "\n".join(lines) + "\n"
