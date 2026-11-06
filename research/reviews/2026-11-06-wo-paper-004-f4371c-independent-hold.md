# REVIEW-M4-INDEP-002 — Architect exact-head independent re-audit (HOLD)

**Date:** 2026-11-06 (Europe/London)  
**Private under-review head:** `f4371c599fb1c45e28c403549090e92fd825ce67`  
**Private PR:** https://github.com/maff0000/paper-bots/pull/5  
**Private base/main at audit:** `b2cb75867d2408a0018333213a0dd2cfb91ac670`  
**Public PR:** https://github.com/maff0000/CGPT-INVESTMENT/pull/9  
**Public PR head verified before this record:** `62769b0206eb11c84a3d618c31106bd106d855c3`  
**Public base/main at audit:** `b0c8f55109fcc92d8f55ec7b593c696b9887475d`

## Decision — HOLD, not acceptance

The earlier `REVIEW-M4-INDEP-001` HOLD of `553ec517455ce6ef797b049e65ec61389daa20da` remains an immutable historical decision. The replacement head `f4371c59` **fixes all three previously blocking replay-integrity findings**, but an independently reproduced malformed-input failure prevents acceptance of this exact head.

## Independent evidence

- Exact private source and tests reconstructed from GitHub tree/blob SHAs, in a separate disposable local directory; no builder worktree used.
- Interpreter Python 3.12.14: `PYTHONPATH=src python3 -m unittest discover -s tests -q` -> **Ran 115 tests; OK** (exit 0). Python 3.9.25 and Python 3.12.3 results are **builder evidence only**.
- Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 independently computed as `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged, entry/exit/stop authority NONE).
- Additional independent, state-preserving probes: missing S parent on replay -> `ValidationError`; false supplied parent hash on replay -> `ValidationError`; changed R quality on replay -> `IdempotencyConflict`; identical S replay -> duplicate; forged S role claim -> `PermissionDenied`. All preserved ledger row count and hash tip.
- Independent **failure**: a valid synthetic E-BOT fixture envelope whose `quality_state` is replaced by an object (`{"unsafe":"UNCHECKED"}`) raises **unhandled `TypeError`**, not `ValidationError`. The quality allowlist membership operation assumes a hashable input. Object and list are legitimate JSON types but invalid quality claims. The ledger stayed unchanged, yet the adapter does not safely reject the malformed envelope through its defined domain error interface. The CLI does not catch `TypeError`.

## Bounded required correction

One new finding `M4-REPLAY-002`: perform an explicit string/type guard before checking quality membership for the E/S/R/M/T native-ingest path. Return controlled `ValidationError` for non-string types and missing values. Add tests for object, list, boolean, number, missing on new writes and replays; assert no ledger mutation and controlled CLI error rather than unhandled traceback. Preserve all existing replay fixes and exact existing accepted values. Do not broaden role, strategy, entitlement, or trade authority. Details were posted to private PR #5: https://github.com/maff0000/paper-bots/pull/5#issuecomment-6681250358

## Unchanged boundaries

- G0 OPEN; data-provider rights UNVERIFIED; FMP remains three historical calls with the third 402 and no fourth call.
- Stop-dependent M-Bot/T-Bot actions HOLD; synthetic M research HOLD and T NO_ORDER only; no fill/order authority.
- Native-app-to-Python transport and protected NEO OS principal not demonstrated; in-process asserted ID is not platform authentication.
- No live account reads, orders, vendor/broker calls, scheduler activation, or merge. Both PRs remain HOLD pending independent exact-head re-audit.

**Next action:** Grok makes only the bounded correction and updates the existing private/public PRs and governance packet, then reports exact new heads. The Architect independently re-audits those heads.