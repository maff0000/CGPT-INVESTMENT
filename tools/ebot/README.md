# E-Bot v0.1

E-Bot is a manual, read-only check for one Massive Stocks Basic trial. It is not an investment agent, a scheduler, a broker client, or a place to store market data.

The command name is `ebot`. The brief's `e_bot` spelling is this same program.

Copy this directory to a private workstation before a live key is used. The public repository is only the review copy. Do not put an API key, a key file, or vendor bars in it.

## Offline tests

From this directory, with Python 3.9 or newer and the standard library only:

```sh
python3 -m unittest discover -s tests -v
```

The tests use fake HTTP responses. They do not call Massive.

## Commands

```sh
python3 -m ebot help
python3 -m ebot run massive-smoke --session 2026-11-04 --from-date 2025-08-01
python3 -m ebot prompt "Check Massive connectivity and 260+ daily bars for XOM, LIN, EQIX, SPY as at 2026-11-04"
```

`./bin/ebot` is the same entry point. A prompt is accepted only when it is the sentence above, with one real session date. `as of`, a trailing full stop, and `and` before `SPY` are accepted as the same sentence. Any other instruction is rejected and makes no network call.

The prompt always uses `--from-date 2025-08-01`. To choose another start date, use `run` and pass `--from-date`. The symbols are fixed: XOM, LIN, EQIX, SPY.

## API key

Do not pass the key on the command line, do not commit it, and do not paste it into chat. E-Bot refuses `--api-key` and any key file inside a git repository or this package directory.

For one run, omit `--key-file`. E-Bot asks in the terminal with a hidden prompt:

```text
Enter Massive API key (input hidden):
```

For repeated manual runs, create a private file outside the repository:

```sh
umask 077
mkdir -p "$HOME/.config/ebot"
chmod 700 "$HOME/.config/ebot"
python3 -c 'import getpass, pathlib; p=pathlib.Path.home()/".config/ebot/massive.key"; p.write_text(getpass.getpass("Massive API key: ").strip()+"\n"); p.chmod(0o600)'
python3 -m ebot run massive-smoke --session 2026-11-04 --from-date 2025-08-01 --key-file "$HOME/.config/ebot/massive.key"
```

Do not use `echo` or a shell history line to write the key. The file must be a regular file, owned by you, mode `0600`, and one line. If stdin is not a terminal and no key file is given, E-Bot exits `2` with `SETUP_NEEDED` and sends nothing.

## What one live run does

After the local checks pass, E-Bot sends at most five read-only HTTPS GET requests to `https://api.massive.com`:

1. Grouped US daily bars for the requested completed session.
2. Daily bars for XOM, LIN, EQIX, and SPY from the start date through that session.

The key is sent only as an `Authorization: Bearer` header. A 401, 403, 429, or other error stops the run. Nothing is retried. Wait at least one minute before starting another manual run. Basic data for a session is requested only after midnight America/New_York on the next calendar day. Weekends are refused locally. A span longer than 731 days is refused locally because published Basic history is two years; that guard is not an account entitlement.

The report lists counts, earliest and latest dates, duplicate and invalid counts, the adjustment convention, and PASS / HOLD / FAIL. It does not print raw bars. `overall PASS` means this access and coverage check only. `g0_acceptance` stays `OPEN`. With one vendor, the price comparison is `SECOND_SOURCE_NOT_TESTED`. The retained rule, for a later two-source check, is: absolute USD close difference `<= 1.00` is `PRICE_OK`, `> 1.00` is `PRICE_CHECK`, a strict pivot straddle is `SIGNAL_AMBIGUOUS` and blocks breakout confirmation, and an instrument, session, currency, or adjustment mismatch is `DATA_MISMATCH`.

Exit codes: `0` PASS, `1` FAIL, `2` SETUP_NEEDED, `3` rejected instruction, `4` HOLD.

## First live provider test

Do this only after these offline tests pass and a person explicitly asks for the live test.

1. Confirm the Massive Stocks Basic account and that its individual-use terms cover this private manual run. Commercial redistribution is a separate decision.
2. Copy this directory to the private Mac. Python 3.9.6 is enough. No extra packages.
3. Pick one completed US session whose next calendar midnight in America/New_York has already passed. `2026-11-04` is the documented example.
4. Supply the key by the hidden prompt or the `0600` file above.
5. Run the `massive-smoke` command once.
6. Keep the text report. Do not copy raw responses, the key, or a price table into the public repository or an external AI chat.
7. A second licensed source is still required before any `PRICE_OK` or `PRICE_CHECK` result. G0 stays open.

## Conflicts recorded with the build

- The brief says not to store this program in the public repository. This tree is the review copy to move onto a private workstation. Keys and vendor bars stay out.
- Prose uses E-Bot. The package and command use `ebot`, not `e_bot`.
- The undated sentence "Check Massive connectivity and historical data availability for XOM, LIN, EQIX and SPY." is rejected as ambiguous. The dated allowlisted sentence is required.
- The existing `g0_massive_readonly_probe.py` script always prompts and calls the network, so it is not imported. E-Bot uses the same host, bearer header, five-call sequence, and paths.
