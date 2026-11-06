# REVIEW-M5-ACCEPT-001 — WO-PAPER-005 Increment A independent exact-head acceptance

**Date:** 2026-11-06 (Europe/London)  
**Architect decision:** **ACCEPT — bounded offline synthetic transport spool and NEO snapshot reader only**. No authenticated native runtime, host ACL, live provider access, scheduler or trade authority is accepted.

## GitHub exact-head and merge record

| Item | Verified SHA / finding |
|---|---|
| [Private paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) accepted exact head | `b87354d77dc4d94273291ae571c3837924f22fdd` |
| Private base / prior accepted `main` | `ff13c49ce2535992c7216f5742946b33bd805e53` |
| **Private normal merge-commit**, verified new `main` | **`ba001debca9e695fc3356c8720a17fa15836c31c`** (no rebase/squash) |
| [Exact-head Architect comment](https://github.com/maff0000/paper-bots/pull/6#issuecomment-6683905971) | ACCEPT for offline Increment A only |
| [Public CGPT-INVESTMENT PR #10](https://github.com/maff0000/CGPT-INVESTMENT/pull/10) before this record | `1891c676b81d72c6103a1fa11c347b3e69c392dd`, base `1fc4491a095d914b855a2653cb8b753c7fbc3f13` |
| Independent suite | Python **3.12.14**, `PYTHONPATH=src python3 -m unittest discover -s tests -q`, **136 tests OK**, exit 0 |
| Builder suites, reported only | Python 3.9.25 and 3.12.3 both 136 OK; not Architect reruns |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`, unchanged, entry/exit/stop authority NONE |

## Independent recovery/integrity probes

Private source, tests and synthetic fixtures were reconstructed from exact GitHub tree/blob hashes in an isolated temporary directory. The Architect ran full-suite and an additional **separate throwaway probe**, not merely the builder's tests.

| Scenario | Verified independent outcome |
|---|---|
| Six fixture submissions E→S→R→M→T→NEO | Six accepted receipts; NEO snapshot hash/chain verifies; T `NO_ORDER`, `is_fill=false` |
| Terminal `accepted` receipt, archive interrupted, staged files unchanged, then restart | Original receipt returned and files archived as accepted; no second append |
| Same interruption, then changed staged envelope bytes | `RECOVERY_INTEGRITY` error, separate recovery record, quarantined bytes, not accepted; primary receipt unchanged |
| Same interruption, then missing sidecar | Controlled recovery failure, quarantine; primary receipt unchanged |
| Same interruption, then corrupt sidecar | Controlled recovery failure, quarantine; primary receipt unchanged |
| Crash after ledger commit but before receipt | Restart returns `duplicate`, no new append |

For each rejected recovery, ledger row count and hash tip were unchanged. Inspection of the last correction showed `_recover_processing` now revalidates successful receipts with the staged sidecar and envelope before archive; no change to the accepted native-ingest decision semantics or frozen manifest.

## Accepted scope

WO-PAPER-005 Increment A provides an **offline, synthetic-only file spool** around the already accepted single Python ledger writer. Submission has an untrusted envelope and separately staged synthetic attestation sidecar; mismatches/unknown IDs fail closed. A lock serializes the spool, with tested restart/replay/outage recovery. An immutable snapshot and content digest allow a read-only NEO API without append methods. The content digest is not a signature and the sidecar is not authentication.

**Not approved/demonstrated:** real native Grok Bot messaging (Increment B), authenticated native sender metadata, a dedicated OS or Cursor user/principal with enforced permissions for writer and NEO (Increment C), live US universe, provider entitlements, scheduled calls, broker/account reads or real trading. Same-user bots still share resources, so in-process checks, spool locks and snapshots are *not* host ACLs.

G0 **OPEN**. Provider rights **UNVERIFIED**. FMP remains three historical calls (third HTTP 402), no fourth call. M-Bot/T-Bot stop-dependent functions **HOLD**; QARP entry, stop and exit authority **NONE**. No new risk parameter, live order, scheduler, vendor call or broker action.

[REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains an immutable correct HOLD **for the older exact head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only**. This acceptance does not edit or withdraw it. [REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) and prior historical HOLDs remain unchanged.

## Next proposed work

Perform separate, bounded discovery/acceptance gates for Increment B genuine native-app delivery and Increment C independently enforced writer/NEO principal. No real bot-message probes, host privilege modifications, scheduling, external provider queries or broker activity without separately approved authority. Grok must record ADRs, tests, exact SHAs and sanitized review packets on GitHub, then stop before merge for independent Architect acceptance.
