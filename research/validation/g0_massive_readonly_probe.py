#!/usr/bin/env python3
"""G0 manual Massive OHLCV connectivity/coverage smoke test. No agent or broker actions.

Uses five read-only REST requests maximum: one grouped day and four ticker series.
Prints only diagnostic counts and dates, never raw vendor prices or the API key.
Requires Python 3.9+ and a Massive Stocks subscription with the requested dates.
"""
import argparse
from datetime import datetime, timezone
from getpass import getpass
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HOST = "https://api.massive.com"
SYMBOLS = ("XOM", "LIN", "EQIX", "SPY")


def fetch(path, api_key):
    req = Request(HOST + path, headers={"Authorization": "Bearer " + api_key})
    with urlopen(req, timeout=35) as response:
        payload = json.load(response)
    if not isinstance(payload, dict):
        raise ValueError("Response was not a JSON object")
    return payload


def main():
    parser = argparse.ArgumentParser(description="Manual G0 price feed trial (5 API calls)")
    parser.add_argument("--date", default="2026-11-04",
                        help="a COMPLETED prior US market session YYYY-MM-DD, default 2026-11-04")
    parser.add_argument("--from-date", default="2025-08-01",
                        help="earliest date for requested ticker bars YYYY-MM-DD")
    args = parser.parse_args()
    for value in (args.date, args.from_date):
        datetime.strptime(value, "%Y-%m-%d")
    if args.from_date >= args.date:
        parser.error("--from-date must be earlier than --date")

    print("Read-only G0 test. API key is not saved or printed.")
    token = getpass("Enter Massive API key (input hidden): ").strip()
    if not token:
        print("No key supplied; no request made.")
        return 2

    try:
        # One grouped market-wide completed-day EOD request.
        grouped = fetch(
            "/v2/aggs/grouped/locale/us/market/stocks/"
            + args.date + "?adjusted=true", token
        )
        records = grouped.get("results") or []
        available = {r.get("T") for r in records if isinstance(r, dict)}
        print("GROUPED", "status=" + str(grouped.get("status")),
              "count=" + str(grouped.get("resultsCount")),
              "samples_present=" + ",".join(s for s in SYMBOLS if s in available))
        if not records or not set(SYMBOLS).issubset(available):
            print("HOLD: grouped data missing one or more test instruments")

        # Four custom ticker ranges. Five calls total, within Basic's 5/min allowance
        # for ONE run. DO NOT immediately rerun or issue more calls in same minute.
        for symbol in SYMBOLS:
            path = ("/v2/aggs/ticker/" + symbol + "/range/1/day/"
                    + args.from_date + "/" + args.date
                    + "?adjusted=true&sort=asc&limit=5000")
            data = fetch(path, token)
            bars = data.get("results") or []
            timestamps = [b.get("t") for b in bars if isinstance(b, dict)]
            unique = len(timestamps) == len(set(timestamps))
            count = len(bars)
            valid = count >= 260 and unique and data.get("status") == "OK"
            first = (datetime.fromtimestamp(min(timestamps) / 1000, timezone.utc)
                     .strftime("%Y-%m-%d") if timestamps else "NONE")
            last = (datetime.fromtimestamp(max(timestamps) / 1000, timezone.utc)
                    .strftime("%Y-%m-%d") if timestamps else "NONE")
            print(symbol, "bars=" + str(count), "unique_dates=" + str(unique),
                  "from=" + first, "to=" + last,
                  "bars>=260=" + str(valid))
        print("Five read-only calls completed. Data has NOT been saved or published.")
        print("Next: reconcile same-date closes with licensed independent source, "
              "then manually validate chart calculations.")
        return 0
    except HTTPError as exc:
        print("HTTP ERROR", exc.code,
              "(401 key, 403 entitlement/current-day, 429 limit are common); "
              "no key or response body printed.", file=sys.stderr)
        return 1
    except (URLError, ValueError, KeyError, TypeError) as exc:
        print("TEST HOLD", type(exc).__name__, "(details withheld)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
