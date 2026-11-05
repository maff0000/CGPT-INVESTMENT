# G0-D3 PR #2 — Architect independent offline review: HOLD
**Date:** 2026-11-05 (Europe/London)
**Repository:** private maff0000/ebot
**Exact candidate:** 9b843dee03892e73f29da31997e5d07bfed564a7
**Base:** 50c0b66247498672b84e9fcae7e417a538a0e5c1
**PR:** https://github.com/maff0000/ebot/pull/2
**Review status:** **HOLD / CORRECTIONS REQUESTED, NOT MERGED**.

## Scope independently checked
The Architect fetched all 31 text files at the exact PR head, reconstructed a private offline snapshot in the review workspace and ran the full standard-library unit suite using Python 3.12.14. **105 tests completed successfully on this local environment** (the builder separately reports 104 pass + one intentionally skipped on Python 3.9.25 and 3.12.3). This Architect made **zero** live Massive, IBKR or broker calls and accessed no credentials or private trading account. Review of E-Bot source indicates read-only market-data methods, fixed four-symbol G0 trial, bounded calls, price tolerance at $1.00 inclusive, SIGNAL_AMBIGUOUS at a pivot straddle, single-source manual-review-only fallback and automated_trading_permitted=false.

## Three reproductions missing from the builder's test path
1. **Malformed real HTTP JSON shape:** production Massive urllib_send rejects JSON-array response as ProviderPayloadError, but fetch_session_closes maps that error to UNAVAILABLE / OUTAGE. A fake in-memory HTTP 200 response with body [] produced UNAVAILABLE / NOT_APPLICABLE / OUTAGE. The test passing a non-object directly through injected transport bypasses that actual parser boundary. This is malformed data, not an evidenced outage.
2. **Malformed grouped ticker:** a returned grouped row with non-text T is silently ignored. When no correctly attributed target row exists, only MISSING_SESSION_BAR is recorded with no provider malformed-identity evidence. We must not guess which ticker the row belonged to, but must retain provider-level INVALID_DATA diagnostics alongside legitimate missing-session state.
3. **Malformed IBKR bar date:** a returned bar for a known contracted symbol with date={} is silently excluded from matches, leading to MISSING_SESSION_BAR with no invalid-timestamp diagnostic. It cannot prove a valid requested-session close, but it is still an invalid returned record.

**Safety assessment:** none of these examples demonstrate live-order access or an automated trading bypass; they are diagnostic integrity/classification gaps at G0. Other unaffected valid symbols must remain usable for manual research, and UNCHECKED must still mean a genuinely unavailable corroboration source rather than malformed response data. G0 stays OPEN.

## Disposition
GitHub rejected a formal REQUEST_CHANGES review because the linked identity is also the PR author (HTTP 422). Architect posted a clearly labelled **HOLD corrective comment** to the PR conversation. This is not a formal protected review and not a merge. The builder must correct the three cases narrowly with offline tests at the actual HTTP and malformed-row paths, explain provider-level versus per-symbol status, report a new exact SHA, then stop for further independent acceptance. No new live vendor calls, exchange-calendar expansion, auto scheduler, bot build or broker scope was authorised by this review.
