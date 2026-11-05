# Architect M2 independent acceptance — QARP screening and NEO causal evidence

**Date:** 2026-11-05 (Europe/London)
**Evidence class:** ARCHITECT-INDEPENDENT
**Disposition:** **ACCEPTED AND MERGED, PAPER CODE ONLY**
**Private repository:** `maff0000/paper-bots`

## Exact refs
- Private [PR #2](https://github.com/maff0000/paper-bots/pull/2) accepted head: `810b6fd48b266031c1b299c39370bf3ececb449b`.
- Base verified before merge: `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`.
- Merge method: normal merge commit with expected-head guard.
- Verified private main after merge: `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d`.
- PR acceptance comment: [paper-bots #2](https://github.com/maff0000/paper-bots/pull/2#issuecomment-6668341862).
- Public governance PR #7 carries this record for Architect review/merge; public main is not automatically changed by the private merge.

## Independent audit
1. Reconstructed all 94 source, test, fixture and documentation blobs from the exact private PR head in an isolated local workspace.
2. Ran `PYTHONPATH=src python3 -m unittest discover -s tests -q` under Python **3.12.14**: **82 tests, OK**.
3. Independently replayed an E-Bot candidate with mutated `source_id`, `quality_state`, `reason_codes` and `uncertainty`. Each correctly returned an explicit conflict; row count and hash tip unchanged.
4. Confirmed a generated clock-only retry remains an accepted idempotent duplicate.
5. Reviewed the prior changed discovery-parent conflict and full E→S→NEO correlation regression cases. These pass, including zero-candidate cohort.
6. Compared the final correction to preceding head `e403f29db0fe74f7b2b5f3ad7d84f160a966df22`: exactly five file paths changed—ledger comparator, new decision-identity tests, README, ADR and bounded WO.
7. Scanned executable sources for networking/broker order access; no new external call or live execution capability found. No vendor or broker calls were made.

The builder's Python 3.9 and 3.12 results remain builder-reported rather than independently replayed by this review.

## Accepted scope
- QARP-ROTATION-001 v1.0.0 deterministic Finviz A/B/C **screen classification** and separate near-miss/unknown paths.
- Append-only ledger v0.2 with provenance and fail-closed semantic idempotency.
- S-Bot discovery-parent references and NEO correlation/cohort evidence for synthetic fixtures.
- Existing M1 mock six-role research chain remains accepted as a foundation.
- Private historical July doctrine preservation was accepted separately; it remains history, not trading policy.

This is acceptance of **software correctness for bounded fixture-driven paper research**. It is not acceptance of investability, a live equity screen, provider feed equivalence, an operational scheduler, or every future bot implementation.

## Remaining blockers and next milestone
- **G0 OPEN**, provider rights and FMP subscription/entitlement unverified; no new vendor calls.
- QARP entry, stop, trailing stop, exit, trims, sizing/risk rules **NOT APPROVED**; stop-dependent M/T paths HOLD.
- No production scheduling, capital deployment or live broker order authority.
- May full doctrine still inaccessible, historical originals are non-canonical.
- Actual Grok Bot **app-visible, individually messageable E/S/R/M/T/NEO teammates** have not been implemented or inspected; this is a distinct owner requirement tracked in [WO-APP-PRESENCE-001](../../work-orders/WO-APP-PRESENCE-001-grok-bot-teammates.md).
- Next work should prioritise **credible all-sector discovery and strategy-evidence interfaces**, app teammate presence within platform constraints and paper-only dry runs. The screening requirements and source entitlements must be proven before any trading-day schedule.
- NEO must continue collecting all pass/reject/near-miss/unknown events, not merely winning paper trades.

**Governance:** GitHub remains the source of truth. Grok has bounded engineering autonomy under the existing PID and roadmap; all material decisions and next WOs must be recorded for independent Architect review.
