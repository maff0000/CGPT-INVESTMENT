# WO-PAPER-004 independent exact-head audit — HOLD

**ID:** REVIEW-M4-INDEP-001  
**Date:** 2026-11-06 (Europe/London)  
**Decision:** **HOLD** pending one bounded semantic/provenance replay correction. No merge.

## Verified heads and evidence

| Item | Value |
|---|---|
| [Private paper-bots PR #5](https://github.com/maff0000/paper-bots/pull/5) | HEAD `553ec517455ce6ef797b049e65ec61389daa20da`, accepted base `b2cb75867d2408a0018333213a0dd2cfb91ac670`, OPEN, unmerged |
| [Public governance PR #9](https://github.com/maff0000/CGPT-INVESTMENT/pull/9) | Reviewed HEAD `22f43d2de1e2da5c6cdeb7347e45c7096a4c21e2`, accepted base `b0c8f55109fcc92d8f55ec7b593c696b9887475d`, OPEN, unmerged |
| Independent suite | Reconstructed private GitHub tree at exact head; **110/110 tests pass**, Python **3.12.14** |
| Other suites | Python 3.9.25 and 3.12.3, 110 tests each, **builder evidence only** |
| QARP file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`, unchanged |

No vendor, broker, account, scheduler, native teammate, or order calls during this review.

## What works

The in-process synthetic E→S→R→M→T→NEO adapter uses the accepted ledger. Role is selected from the caller-supplied allowlisted UUID rather than the JSON producer claim. E is UNCHECKED, frozen S QARP has entry authority NONE, R/M HOLD, T records NO_ORDER and NEO can write NEO_REVIEW through this ingest. The code honestly reports caller-supplied UUIDs as **not authenticated native platform metadata**, and NEO host ACL remains unimplemented.

## Independently reproduced replay fidelity defects

All probes used the synthetic fixture and the actual new Python ingest, with earlier steps already stored.

1. Replay S with the same idempotency key after **removing `parent_event_id`**. Result `duplicate: true`. The replay helper silently substitutes a stored parent despite the normally required causal claim.
2. Replay S with **`parent_event_hash` set to 64 zeroes**. Result `duplicate: true`. An explicitly incorrect hash is ignored instead of rejected.
3. Replay R with **`quality_state` changed from `NOT_APPLICABLE` to `UNCHECKED`**. Both values pass input validation; the synthesised event remains NOT_APPLICABLE and replay returns `duplicate: true`.

Ledger count and hash tip remain unchanged: this is **input-to-evidence fidelity**, not ledger deletion. Earlier accepted M2 replay doctrine requires changed quality and causal evidence to conflict or be rejected, not silently counted as equivalent. The allowed free-text `note` is also ignored by the emitted decision; specify clearly if it is intentionally non-semantic diagnostic text.

## One bounded correction

[Private PR #5 exact-head corrective review](https://github.com/maff0000/paper-bots/pull/5#issuecomment-6680880523). GrokBot should keep the current PR and make new/replay parent validation equivalent, validate supplied hashes on replay, and either constrain role-specific quality claims or incorporate validated quality into decision identity. Explicitly identify ignored non-semantic envelope fields, then test missing parent, bad parent hash, changed quality both ways, exact retries, rejected writes unchanged and no-order/NEO protections. Update the ADR, tests and governance PR #9. Do not merge.

## Unchanged boundaries

Accepted M3 stays merged: private `b2cb75867d2408a0018333213a0dd2cfb91ac670`; public `b0c8f55109fcc92d8f55ec7b593c696b9887475d`. Native-to-Python live execution and protected NEO OS isolation remain **UNVERIFIED/UNIMPLEMENTED**. G0 OPEN; provider rights UNVERIFIED; stop-dependent M/T HOLD; no scheduler or real order authority. This review does not approve risk or policy.
