# WO-PAPER-005 — recovery-integrity correction, Increment A

**ID:** REVIEW-M5-TRANSPORT-002  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for a bounded correction on the open private pull request.  
**Disposition requested:** Architect **ACCEPT or HOLD** of exact private head `b87354d77dc4d94273291ae571c3837924f22fdd`.  
**This packet does not accept that head.** It does not merge private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) or public [PR #10](https://github.com/maff0000/CGPT-INVESTMENT/pull/10). Builder **136/136 is not Architect acceptance**. This correction does not authenticate native senders and does not implement a host access-control list.

[REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains the HOLD of `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` for M5-RECOVERY-001. That HOLD is valid only for that older exact head. The file is not edited here. [REVIEW-M5-TRANSPORT-001](2026-11-06-wo-paper-005-offline-transport-packet.md) stays the historical request for that same head and is not edited here.

[REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains accepted history for the offline in-process adapter only, paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`. [REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Those older HOLDs are valid only for those exact heads. None of those files is edited here.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-005-transport-packet-f3e8` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `1fc4491a095d914b855a2653cb8b753c7fbc3f13`. Public PR #10 head `4d7a24c17727912ed1efd9e36af61059bc354355`, which is the parent of this public commit. The six Architect HOLD commits after `ea5a216e071a58a0bb820c810bbdb85be61466b1` are still on the branch |
| Parent-verified private read-back, 2026-11-06 Europe/London | Private PR #6 state, both private SHAs, the correction's parent, the sanitised recovery rule, the six-file change size, and the builder test transcript |
| Not claimed here | Architect acceptance of `b87354d7`, withdrawal of REVIEW-M5-INDEP-001, a merge, native-sender authentication, a host access-control list, vendor rights, or a fourth FMP call |

This public session did not open `maff0000/paper-bots` and did not copy private source, fixtures, class names, function names, import paths, or source excerpts.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main`, unchanged, and PR #10 base | `1fc4491a095d914b855a2653cb8b753c7fbc3f13` |
| Public PR #10 head before this write, and parent of this public commit | `4d7a24c17727912ed1efd9e36af61059bc354355` |
| Public branch | `cursor/wo-paper-005-transport-packet-f3e8` |
| Private pull request | [paper-bots #6](https://github.com/maff0000/paper-bots/pull/6) |
| Private state | OPEN, not draft, `merged` false, `merged_at` null, mergeable clean |
| Held older private head, REVIEW-M5-INDEP-001 | `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` |
| Parent of the new private commit | `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` |
| Private head under review | `b87354d77dc4d94273291ae571c3837924f22fdd` |
| Private commit message | Revalidate successful spool recovery before archive. |
| Unchanged paper-bots main and PR base | `ff13c49ce2535992c7216f5742946b33bd805e53` |
| Private PR versus accepted main | 2 commits, 23 files, +2043 / −3 |
| This private correction only | 6 files, +312 / −12 |
| Public note | [WO-PAPER-005](../../work-orders/WO-PAPER-005-native-transport.md) |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |

## What the HOLD recorded

REVIEW-M5-INDEP-001 of exact `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` found M5-RECOVERY-001. After a durable successful receipt, restart could archive later-altered staged envelope bytes as accepted. The ledger tip did not change, so the archived evidence no longer matched the committed decision. No distinguishable recovery error was recorded. That finding stays the decision for that older head.

## Correction

Parent-read behaviour, not an Architect confirmation. A terminal successful receipt, `accepted` or `duplicate`, no longer authorises archive by itself. Recovery rechecks the staged envelope and attestation against the durable receipt before archiving. The recheck covers the envelope SHA-256, the submission id, the attested native identity, the source, and the transport contract.

On a match, archive proceeds and the stored receipt is returned. On a mismatch, a missing sidecar, or a corrupt sidecar, the original receipt is left untouched. The mismatching evidence is retained and quarantined rather than archived as accepted or duplicate. A separate recovery record is written beside the receipt, with `kind` `RECOVERY_INTEGRITY`. The ledger is not appended to. Row count and hash tip stay unchanged.

Matching recovery stays intact. A crash before the receipt still recovers as `duplicate` with no second append. Retryable ledger-outage behaviour stays intact: a retryable ledger write failure returns the submission to the inbox. Terminal rejection archive behaviour is unchanged.

Quarantine retains the mismatching bytes. It is not a host access-control list.

## What changed, at a high level

The correction commit touches documentation and the offline transport implementation and its tests. The documentation is the private README, the runbook, the offline-transport decision record, and the private work-order note. The implementation and test paths are not named here. No private source is copied.

## Tests

Parent-confirmed builder transcript. Not an Architect run. Detached worktree at `b87354d77dc4d94273291ae571c3837924f22fdd`. Command `PYTHONPATH=src python3.X -m unittest discover -s tests -v`. Stdout 0 bytes on both. The held head had 132 tests.

| Interpreter | Exit | Wall | Stderr |
|---|---|---|---|
| Python 3.9.25 | 0 | 1.954s | `Ran 136 tests in 1.615s` / OK |
| Python 3.12.3 | 0 | 1.266s | `Ran 136 tests in 1.108s` / OK |

**Builder 136/136 is not Architect acceptance.**

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, broker or account read, vendor call, or trade-policy approval is granted.
- No bot message was sent. No host principal was changed.

## Limitations

- This correction does not authenticate native senders and does not implement a host access-control list.
- Quarantine is retention of mismatching evidence. It is not an access-control list.
- The snapshot hash detects truncation and is not a signature.
- Increments B and C remain gated and are not implemented.
- Paper-bots main is unchanged at `ff13c49ce2535992c7216f5742946b33bd805e53`. Public main is unchanged at `1fc4491a095d914b855a2653cb8b753c7fbc3f13`. Private PR #6 and public PR #10 stay open.

## Restrictions

This packet authorises none of the following:

- acceptance of `b87354d77dc4d94273291ae571c3837924f22fdd`
- withdrawal of the HOLD of `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`
- merge of private PR #6 or of public PR #10
- native-sender authentication or a host access-control list
- live orders, broker writes, or account reads
- vendor calls
- a scheduler or activation
- new entry, exit, stop, or risk parameters

## Proposed disposition

Request an Architect re-audit of exact private head `b87354d77dc4d94273291ae571c3837924f22fdd`, then an **ACCEPT** or **HOLD** recorded against that SHA. Until that independent review exists, the correction stays proposed. Passing builder tests and this public packet are review inputs. They are not the decision.

Rollback of an unaccepted correction is to leave paper-bots main at `ff13c49ce2535992c7216f5742946b33bd805e53` and public main at `1fc4491a095d914b855a2653cb8b753c7fbc3f13`. This file does not perform either merge.
