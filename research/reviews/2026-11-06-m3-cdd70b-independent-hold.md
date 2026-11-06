# M3 independent correction re-audit — HOLD

**ID:** REVIEW-M3-INDEP-002  
**Date:** 2026-11-06 (Europe/London)  
**Architect decision:** **HOLD** — one narrow fallback-regression correction required. Neither PR merged.

## Exact-head evidence

| Item | Verified value |
|---|---|
| [Private paper-bots PR #4](https://github.com/maff0000/paper-bots/pull/4) | HEAD `cdd70b02a2c53ce25db9b857d03590491f247771`, accepted main/base `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d`, OPEN |
| [Public governance PR #8](https://github.com/maff0000/CGPT-INVESTMENT/pull/8) | Reviewed HEAD `6e4196484b85f0c42a54e149e632f02c9f158b63`, accepted main/base `20094068e20c2de0a659e8243657207c8d4cfbaa`, OPEN |
| Independent code verification | Reconstructed GitHub tree at private exact head; **96 of 96 tests OK** on Python **3.12.14** |
| Other Python verification | Python 3.9.25 and 3.12.3: 96 tests OK **builder-reported only**; independent 3.9 interpreter unavailable in this environment |
| QARP manifest SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`, matches prior accepted strategy |

The four defects in [REVIEW-M3-INDEP-001](2026-11-05-m3-a40412f-independent-hold.md) are corrected in the submitted source: conflicting provider dedup, OTC annotation dependence, stale corroboration and malformed source entry handling. The full 96-test suite is green. No vendor, broker, account, scheduler or order calls were made.

## New reproducible regression — fallback semantics

The amended `src/paperbots/discovery/prepare.py` no longer gives FAILED sources their agreed fallback effect. The independent re-audit used a copy of `us_equity_fixture_v0`, a nonproduction universe ID and only synthetic source rows.

1. **Two aligned PRESENT sources + third distinct FAILED source with null timestamp** yields **`ADMITTED`**. The previous implementation treated *any failed source in a comparison* as `UNCHECKED`, consistent with Matt's instruction to preserve reviewability but block T-Bot automatic trading when a source is unavailable. The new `len(aligned)>=2` branch overlooks the failure.
2. **One aligned PRESENT source + one distinct FAILED source with `as_of_utc: "bad-timestamp"`** yields **`INVALID`**. Timestamp validation is performed on FAILED rows as if they were observed prices. The otherwise valid surviving price should remain **`UNCHECKED`**, with a diagnostic to investigate provider availability; malformed timestamps on PRESENT prices must still be rejected.

Both results are independently reproduced despite 96 passing tests. This is a bounded regression to the already agreed single-source/failed-source policy, **not** an invitation to weaken `DATA_MISMATCH` on contradictory same-provider evidence.

## Narrow corrective work and acceptance

[Exact-head Grok correction on PR #4](https://github.com/maff0000/paper-bots/pull/4#issuecomment-6679116795).

- Explicitly classify source unavailability before `ADMITTED` while maintaining `DATA_MISMATCH` on contradictory observations for one source ID.
- Timestamp quality for FAILED records must not invalidate a valid surviving PRESENT record. Record source failure and a diagnostic, retain raw evidence where policy allows.
- Tests for 2 PRESENT + FAILED; PRESENT + FAILED malformed timestamp; only FAILED; bad PRESENT timestamp; same-source contradiction; no automated-path promotion, no ledger or hash-tip corruption.
- Retest on Python 3.9 and 3.12 and return exact new heads; update this governance packet and statuses. **No self-merge.**

## Unchanged boundaries

M3 is an offline synthetic discovery and provisional native-role chat milestone, not acceptance of a real US equity universe, native-to-Python ledger bridge, protected read-only NEO or platform access control. G0 OPEN; FMP and other provider rights UNVERIFIED; equity entry/exit/initial-stop/trailing-stop/risk policy unapproved; stop-dependent M/T HOLD; scheduling and live execution NOT AUTHORISED. Historical accepted E-Bot and QARP versions are unchanged.

This record supersedes the builder-ready status for exact head `cdd70b02a2c53ce25db9b857d03590491f247771`, while preserving the earlier review as history.
