# Architect exact-head audit — paper-bots M2 and private doctrine evidence
**ID:** REVIEW-PAPER-002-INDEPENDENT
**Date:** 2026-11-05 (Europe/London)
**Public governance:** [PR #7](https://github.com/maff0000/CGPT-INVESTMENT/pull/7), open/unmerged. This is an independent Architect result, distinct from the Grok builder packet.

## Verified exact refs and dispositions
| Target | Exact reviewed head / base | Independent result | Disposition |
|---|---|---|---|
| [paper-bots PR #2](https://github.com/maff0000/paper-bots/pull/2) | head `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4`; base accepted main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | Full source reconstructed from GitHub blobs and 72 tests OK, offline Python 3.12.14; prior swapped-symbol and partial-cohort tests pass, but two new causal-integrity defects reproduced | **HOLD**; not merged |
| [paper-bots PR #3](https://github.com/maff0000/paper-bots/pull/3) | head `531967980bcec40576d929ce32f8bb9900e498f6`; base `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | Eight paths, documentation-only. Four SHA-256 source/evidence hashes independently match the private manifest. Focused privacy pattern scan clear. No executable change | **ACCEPTED FOR PRIVATE PRESERVATION ONLY**; merge commit `928b6967b31ad4bf3b3404cf04b1978c25aaff6d` |
| [E-Bot PR #2](https://github.com/maff0000/ebot/pull/2) | historical accepted private main `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | Not retested during this audit | Previously **code accepted**, G0 open |
| paper-bots PR #1 | historical accepted private main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | Prior independent 52-test acceptance; not a new retest of PR #1 | Previously **mock foundation accepted** |

All source tests were offline. The initial independent reconstruction added an unintended extra trailing blank line in the local committed example summary, causing one golden-text assertion to fail; removing that reconstruction-only blank line yielded 72/72 OK. GitHub source remained unmodified. This is not a claimed Python 3.9 independent run.

## M2 HOLD findings, reproducible
1. **Parent changes hidden by replay.** Two valid E-Bot CANDIDATE events for the same ticker/correlation/session but distinct IDs: first `append_screen` stores parent A; second `append_screen` with the identical run and observation but claimed parent B returns the event still linked to A. Same `idempotency_key` and output payload hash mask changed `parent_event_ids` and `input_hashes`; the change is silently ignored rather than rejected. Independent reproduction confirmed the ledger row count did not change, but the caller's provenance was not honoured. Require immutable-input equivalence (including parents) on replay.
2. **NEO correlation diverges from its parents.** In a successful two-candidate path, E-Bot and S-Bot share correlation `6ba7b811-9dad-11d1-80b4-00c04fd430c8` while NEO_COHORT emits `38419ad5-ca56-549a-941e-a63876457e5a` from `correlation_id_for(run_id)`. Parent IDs still exist, but same-chain correlation joins fail. Carry through the validated source correlation, preserving zero-candidate behavior and rejecting incompatible run metadata.

Formal PR #2 finding: [Architect comment](https://github.com/maff0000/paper-bots/pull/2#issuecomment-6667409366). Grok must correct both with adversarial offline tests, a new exact head, and bounded evidence before Architect re-review. After PR #3 merge, revalidate PR #2 against the new main and merge it non-destructively if necessary; do not force-push or merge unaccepted code.

## Private evidence acceptance limitations
The two July originals are preserved byte-for-byte as handed over; all four hashes match the manifest. The historical original path within private argus commit `46b4d8c8f17490357c6d1536c5027e45341b7f11` was not independently verified, so original-source provenance remains REPORTED. The May full doctrine was not recovered. The proposed equities doctrine is DRAFT, not policy; stop and trailing rules are not approved.

## Unchanged hard gates
- `entry_authority=NONE`; stop-dependent M-Bot/T-Bot remains HOLD, no live brokerage or orders.
- G0 remains OPEN; G1–G3 and prospective utility validation unproven.
- FMP subscription, data entitlement, licence, and redistribution rights unverified; no extra vendor calls.
- No autonomous scheduling, live trading, or rule invention approved.
- Public GitHub contains only sanitised statuses and evidence identifiers; raw private doctrine remains private.
