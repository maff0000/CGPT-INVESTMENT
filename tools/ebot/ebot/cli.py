"""Human-invoked command line for E-Bot v0.1.

Commands are help, one allowlisted run, and one allowlisted prompt.
Nothing in a prompt is passed to a shell.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from getpass import getpass
from typing import Optional, TextIO

from ebot import __version__
from ebot.errors import SecretSetupError
from ebot.massive import DEFAULT_FROM_DATE, DEFAULT_SESSION, preflight, run_smoke
from ebot.prompts import format_rejection, parse_prompt
from ebot.redact import redact
from ebot.report import format_report
from ebot.secrets import credential_on_command_line, resolve_api_key

HELP_TEXT = """E-Bot v0.1
Manual, read-only Massive data checks for G0. Not an investment agent.

Commands
  ebot help
      Show this text.
  ebot run massive-smoke --session YYYY-MM-DD --from-date YYYY-MM-DD
      One grouped US daily request plus daily bars for XOM, LIN, EQIX and SPY.
      Defaults are --session {session} and --from-date {from_date}.
  ebot prompt "Check Massive connectivity and 260+ daily bars for XOM, LIN, EQIX, SPY as at YYYY-MM-DD"
      Map that phrase onto the same massive-smoke task and print the interpretation first.
      Add --key-file PATH to either run or prompt when not using the hidden prompt.

Restrictions
  Only the massive-smoke task is allowlisted. Other prompts are rejected.
  Prompts are never shell commands, Python, URLs, file paths or extra API calls.
  HTTP is read-only HTTPS GET to api.massive.com with an Authorization bearer header.
  One manual run makes at most 5 requests and does not retry 401, 403, 429 or other errors.
  Basic history is about two years. A completed session is available after midnight America/New_York on the next calendar day.
  The report prints counts, dates and states. It does not print raw bars or the API key.
  A missing key is SETUP_NEEDED. No dummy success is reported.
  Price rule retained for a later two-source check: <= $1.00 PRICE_OK, > $1.00 PRICE_CHECK.
  A pivot straddle is SIGNAL_AMBIGUOUS and blocks breakout confirmation. One vendor reports SECOND_SOURCE_NOT_TESTED.
  G0 stays OPEN. This tool does not schedule work, scrape Finviz, connect to a broker, size a portfolio, or place trades.
  Version {version}.
""".format(session=DEFAULT_SESSION, from_date=DEFAULT_FROM_DATE, version=__version__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ebot", add_help=True)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("help", help="show allowlisted commands and restrictions")
    run = sub.add_parser("run", help="run one allowlisted task")
    run.add_argument("task")
    run.add_argument("--session", default=DEFAULT_SESSION)
    run.add_argument("--from-date", default=DEFAULT_FROM_DATE)
    run.add_argument("--key-file", default=None)
    prompt = sub.add_parser("prompt", help="map one allowlisted instruction")
    prompt.add_argument("text", nargs="+")
    prompt.add_argument("--key-file", default=None)
    return parser


def main(
    argv: Optional[list[str]] = None,
    *,
    transport_factory=None,
    prompter=None,
    now: Optional[datetime] = None,
    stdin: Optional[TextIO] = None,
    stdout: Optional[TextIO] = None,
    stderr: Optional[TextIO] = None,
) -> int:
    args_list = list(sys.argv[1:] if argv is None else argv)
    out = stdout or sys.stdout
    err = stderr or sys.stderr
    if credential_on_command_line(args_list):
        err.write(
            "Refusing a credential on the command line. "
            "Use the hidden prompt or a mode-0600 key file outside any git repository.\n"
        )
        return 3
    if not args_list or args_list[0] in {"help", "-h", "--help"}:
        out.write(HELP_TEXT)
        return 0
    parser = build_parser()
    try:
        parsed = parser.parse_args(args_list)
    except SystemExit as exc:
        code = exc.code
        return 3 if code not in (0, None) else 0
    if parsed.command == "help":
        out.write(HELP_TEXT)
        return 0
    clock = now or datetime.now(timezone.utc)
    if parsed.command == "prompt":
        decision = parse_prompt(" ".join(parsed.text))
        if not decision["accepted"]:
            out.write(format_rejection(decision))
            return 3
        out.write(decision["detail"] + "\n")
        return _execute(
            decision["session"],
            decision["from_date"],
            parsed.key_file,
            transport_factory=transport_factory,
            prompter=prompter,
            now=clock,
            stdin=stdin,
            stdout=out,
            stderr=err,
        )
    if parsed.command == "run":
        if parsed.task != "massive-smoke":
            out.write(format_rejection(parse_prompt(parsed.task)))
            return 3
        return _execute(
            parsed.session,
            parsed.from_date,
            parsed.key_file,
            transport_factory=transport_factory,
            prompter=prompter,
            now=clock,
            stdin=stdin,
            stdout=out,
            stderr=err,
        )
    out.write(format_rejection(parse_prompt("")))
    return 3


def _execute(
    session: str,
    from_date: str,
    key_file: Optional[str],
    *,
    transport_factory,
    prompter,
    now: datetime,
    stdin: Optional[TextIO],
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    blocked = preflight(session, from_date, now)
    if blocked is not None:
        stdout.write(format_report(blocked, []))
        return _exit_code(blocked["overall"])
    stream = stdin or sys.stdin
    secrets: list[str] = []
    try:
        api_key = resolve_api_key(
            key_file,
            stdin_is_tty=bool(stream.isatty()),
            prompter=prompter or getpass,
        )
    except SecretSetupError as exc:
        stderr.write(redact(str(exc) + "\n", secrets))
        stdout.write("overall: SETUP_NEEDED\nrequest_sent: no\n")
        return 2
    if api_key:
        secrets.append(api_key)
    try:
        report = run_smoke(
            session,
            from_date,
            api_key,
            now=now,
            transport_factory=transport_factory,
        )
    except Exception as exc:
        stderr.write("unhandled_error: " + type(exc).__name__ + "\n")
        stderr.write(redact("overall: FAIL\nrequest_sent: unknown\n", secrets))
        return 1
    stdout.write(format_report(report, secrets))
    return _exit_code(report["overall"])


def _exit_code(overall: str) -> int:
    if overall == "PASS":
        return 0
    if overall == "FAIL":
        return 1
    if overall == "SETUP_NEEDED":
        return 2
    if overall == "HOLD":
        return 4
    return 1
