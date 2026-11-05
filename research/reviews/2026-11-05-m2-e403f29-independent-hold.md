# Independent M2 audit — e403f29: semantic replay integrity HOLD
**Date:** 2026-11-05 (Europe/London)
**Class:** ARCHITECT-INDEPENDENT
**Repository:** private `maff0000/paper-bots`
**Pull request:** [#2](https://github.com/maff0000/paper-bots/pull/2)
**Exact head:** `e403f29db0fe74f7b2b5f3ad7d84f160a966df22`
**Exact accepted base:** `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`
**Disposition:** **HOLD**, no merge.

## Verification and improvements
The Architect independently reconstructed the full GitHub source snapshot at the head above, inspected the replay and NEO correlation implementations, and ran `PYTHONPATH=src python3 -m unittest discover -s tests -q` offline on Python **3.12.14**. Result: **73 tests OK**. Python 3.9.25 and 3.12.3 successes remain builder-reported, not independently re-run. No vendor or broker calls were made.

The two previous independent blockers are fixed for their reproduced cases:
- Replaying an S-Bot screen against a different valid E-Bot discovery parent now raises and leaves ledger count and hash tip unchanged.
- NEO_COHORT now preserves the same correlation ID as the validated upstream E-Bot/S-Bot screen chain, including explicit zero-candidate cases.

## One additional independently reproduced defect
The shared-ledger `same_recorded_identity` function checks selected immutable fields, but omits decision-semantic `source_id` and `quality_state`. Replaying a stored E-Bot CANDIDATE with the same idempotency key, parent set and payload while changing only one envelope value returns `duplicate=True`, `conflict=False`:
- Old source `FIXTURE_SRC_A+FIXTURE_SRC_B`; caller now claims `REPLACED_PROVIDER_UNVERIFIED`: silently accepted as prior source.
- Old quality `PRICE_OK`; caller now claims `UNCHECKED`: silently accepted as prior PRICE_OK.
The ledger row count remains unchanged but the evidence drift is not rejected or represented. This is material to source-quality auditing and may make downstream replay consumers mistake stale decisions for current evidence. An entitlement mutation already raises from schema validation.

**Required bounded fix:** consistent immutable decision-semantic replay comparison for both single and atomic batch appends, including source, quality, reasons/checks, action, uncertainty, candidate/entitlement metadata as applicable. Distinguish generated retry timestamps from changed underlying evidence. Test exact replay and adverse source/quality claims, with unchanged row count and hash tip for rejects. Do not invent entry/risk policy or broaden provider access.

**Exact corrective instructions:** [Architect PR #2 comment](https://github.com/maff0000/paper-bots/pull/2#issuecomment-6668063602). GROK has bounded design autonomy and must return new head/base, tests, ADR if necessary and updated governance record. PR #2 and this public governance PR #7 remain OPEN/UNMERGED pending independent re-review.

## Unchanged accepted state and gates
- E-Bot code accepted at private main `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`; G0 remains OPEN.
- M1 mock foundation and private July doctrine evidence preservation accepted; paper-bots main remains `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`. This is **preservation only**, not stop policy.
- May full legacy doctrine unrecovered; proposed equities doctrine NOT APPROVED.
- FMP rights/entitlements unverified; no scheduling, real orders, or live trading authority; stop-dependent M/T HOLD.
