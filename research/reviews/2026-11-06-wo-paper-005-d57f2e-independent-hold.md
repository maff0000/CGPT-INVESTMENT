# REVIEW-M5-INDEP-001 — WO-PAPER-005 Increment A independent exact-head HOLD

**Date:** 2026-11-06 (Europe/London)  
**Decision:** **HOLD** private `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` — one independently reproduced crash-recovery evidence-integrity issue.  
**Private PR:** https://github.com/maff0000/paper-bots/pull/6  
**Private base / unchanged main at audit:** `ff13c49ce2535992c7216f5742946b33bd805e53`  
**Public PR:** https://github.com/maff0000/CGPT-INVESTMENT/pull/10  
**Public head checked before this record:** `ea5a216e071a58a0bb820c810bbdb85be61466b1`  
**Public base/main at audit:** `1fc4491a095d914b855a2653cb8b753c7fbc3f13`

## Independent verification

- Independently reconstructed private source/test/fixture/schema bytes from the GitHub tree of exact `d57f2e32`, not the builder's worktree.
- Python 3.12.14 `PYTHONPATH=src python3 -m unittest discover -s tests -q`: **132 tests, OK, exit 0**. Builder Python 3.9.25 / 3.12.3 reported 132 OK each; these are builder results only.
- Frozen QARP-ROTATION-001 v1.0.0 manifest SHA-256 independently matches `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`; strategy entry/exit/stop authority NONE.
- Separate Architect probes: fixture E→S→R→M→T→NEO produces six accepted receipts, hash-valid snapshot, read-only NEO explanation, and T `NO_ORDER` / `order_created=false` / `is_fill=false`. Injected crash after commit and before receipt recovers as `duplicate` without a second append.

## Blocking finding M5-RECOVERY-001

The spool archives a changed/mismatching processing envelope as **accepted** if a terminal receipt already exists.

**Minimal reproducible sequence at this exact HEAD:**

1. Submit a legitimate synthetic E envelope and matching attestation sidecar to a fresh spool.
2. Inject a failure in `NativeTransportWriter._archive` after the ledger commit and `_store_receipt` have succeeded. A durable `accepted` receipt exists; files remain in `processing/<submission_id>`.
3. Change only that processing directory's `envelope.json` to a different JSON object, leaving the sidecar unchanged. Its SHA-256 now disagrees with the sidecar and the accepted receipt.
4. Restart using a fresh writer and call `drain()`.

**Observed:** `drain()` returns an empty result; the ledger stays at one event with unchanged tip; the changed `envelope.json` is silently moved to `accepted/<submission_id>`, while the receipt remains `accepted`. No error or conflict receipt is produced. The archived evidence does not match the committed decision.

**Cause:** `_recover_processing()` sees the terminal receipt and archives directly without revalidating processing bytes against the sidecar and stored receipt. This is an offline crash/restart data-integrity gap, independently of the already disclosed absence of host ACL/authentication.

## Bounded correction

For a processing item with a terminal successful (`accepted`/`duplicate`) receipt, recheck the envelope, attestation, submission ID, attested native ID, source and SHA-256 against the durable receipt **before** archiving as accepted/duplicate. On mismatch or missing/corrupt file, preserve the original receipt, retain/quarantine the changed evidence and emit distinct controlled recovery conflict/error evidence. Never accept/archive mismatched evidence, overwrite the original accepted receipt, append again, or mutate the ledger. Preserve clean terminal-receipt recovery and existing terminal rejection semantics. Add targeted regression tests, both supported Python suites, and docs updates.

Exact reproduction and correction instructions: https://github.com/maff0000/paper-bots/pull/6#issuecomment-6683142810

## Unchanged authority

Previously accepted M4 `541f3f175da8ec684f942dea767a1352cf5df0fb` / private merge `ff13c49ce2535992c7216f5742946b33bd805e53` remains accepted; older M4 HOLDs remain correct historical decisions only for their exact earlier heads. No M5 merge or broader acceptance occurs.

Increment A is still offline synthetic transport. Native app authentication, live native messaging and a protected NEO host principal remain UNVERIFIED/NOT IMPLEMENTED. G0 OPEN; provider rights UNVERIFIED; FMP remains three historical calls (third 402), no fourth call; stop-dependent M/T HOLD; no scheduler, new entry/exit/stop/risk rule, vendor/broker/account call, order or fill.

**Next:** Grok corrects only M5-RECOVERY-001 on existing private PR #6 and public PR #10, records exact new heads, and stops for independent Architect re-audit.