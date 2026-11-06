# M3 — independent exact-head acceptance and private merge

**ID:** REVIEW-M3-ACCEPT-001  
**Date:** 2026-11-06 (Europe/London)  
**Architect disposition:** **ACCEPTED — bounded offline M3 software and fixture only**. This decision neither authorises automated trading nor asserts native runtime integration.

## Exact-head and merge record

| Item | Verified SHA / finding |
|---|---|
| [paper-bots PR #4](https://github.com/maff0000/paper-bots/pull/4) accepted head | `70a673f973bd52155d495f6873eb417374f4948b` |
| paper-bots previously accepted `main` / base | `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d` |
| paper-bots **merge commit**, remotely verified `main` | **`b2cb75867d2408a0018333213a0dd2cfb91ac670`** (ordinary merge-commit, no squash/rebase) |
| [Governance PR #8](https://github.com/maff0000/CGPT-INVESTMENT/pull/8) reviewed pre-acceptance head | `02151541e1d559cf73576c29dbee1382134210b7` against public accepted main `20094068e20c2de0a659e8243657207c8d4cfbaa` |
| Independent full suite | **97/97 tests OK**, reconstructed exact private GitHub tree, Python **3.12.14** |
| Other interpreter suites | Python 3.9.25 and 3.12.3 reported **97 OK** by builder; not independently rerun in Architect environment |
| QARP strategy manifest SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |

[Private exact-head acceptance comment](https://github.com/maff0000/paper-bots/pull/4#issuecomment-6679446914).

## Independent fallback probes

At accepted private head the Architect called the actual fixture classifier with synthetic rows; outcomes:

| Fixture condition | Observed disposition | Automated path |
|---|---|---|
| 2 aligned PRESENT providers + 1 distinct FAILED | `UNCHECKED`, `FAILED:FIXTURE_SRC_C` | BLOCKED |
| 1 aligned PRESENT + 1 FAILED with malformed timestamp | `UNCHECKED`, `FAILED_TIME:FIXTURE_SRC_B` | BLOCKED |
| Only FAILED providers | `SOURCE_UNAVAILABLE` | BLOCKED |
| Invalid timestamp on PRESENT observation | `INVALID` | BLOCKED |
| Conflicting PRESENT and FAILED reports for same source ID | `DATA_MISMATCH` | BLOCKED |
| 2 distinct aligned PRESENT and no failed source | `ADMITTED` | BLOCKED (paper fixture) |

All six probes returned `trading_permission: false`. Earlier duplicate-order, OTC, stale, typed malformed input, replay and ledger tests passed. No network/broker client imports appeared in the scanned source package. No vendor, broker, account, scheduler, or order calls were made during this audit.

## Scope accepted

- Offline 16-synthetic-instrument, 11-sector broad discovery fixture: no seven-name cap and no claim of actual US listing-universe coverage.
- Source identity, listing exclusion, stale and failed-source rules; all outcomes and provenance remain reviewable, with UNCHECKED fallback not promoted to trading authority.
- Existing accepted QARP-ROTATION-001 v1.0.0 invoked **after** discovery; frozen screening rule unchanged.
- Offline paper-bot ledger, deterministic role contracts, S-Bot screen and NEO discovery/cohort digest; versioned synthetic evidence.
- Native Grok app identities and message receipts remain **operator-/parent-reported bounded chat evidence**. The typed offline contract is accepted as a proposed interface, **not** proof of app-level access control or live native-to-ledger execution.

## Explicit non-acceptances and next work

- **G0 OPEN**; no licensed real US universe. Finviz, FMP, Massive, IBKR provider rights and quotas not newly verified; FMP still only **three historical calls**, last HTTP 402.
- **Native-to-Python ledger execution NOT VERIFIED**. Protected NEO isolation and hard role ACL **NOT IMPLEMENTED/NOT VERIFIED**. Do not equate instructional persona refusals with security controls.
- May historical full text unavailable. Equity entry, exit, initial-stop, trailing-stop, sizing/risk doctrine not approved. Stop-dependent M/T management remains **HOLD**.
- No automated scheduling, live broker orders, account reads, credential changes or real-money trading.
- Next governed increment: explicit source-rights/licence evidence and a bounded *offline* native-to-ledger/NEO interface demonstration, followed by real-universe design and supervised paper research when entitlements are verified. No authority to begin scheduled live discovery from this acceptance alone.

This acceptance supersedes the earlier HOLDs **only for this accepted head**. The prior audit results at `a40412f` and `cdd70b02` remain historical evidence. GitHub is the handoff truth; use exact HEADs before future work.
