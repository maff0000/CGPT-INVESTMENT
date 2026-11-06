# WO-PAPER-005 — offline native transport (public note)

> **CURRENT ARCHITECT DECISION — WO-PAPER-005 INCREMENT A HOLD (6 Nov 2026).** The independent review **HOLDs** private paper-bots PR #6 exact head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` after 132/132 independently run Python 3.12.14 tests and a separate crash/recovery probe that found a corrupted processing envelope silently archived as `accepted` when a terminal receipt exists. Read [REVIEW-M5-INDEP-001](https://github.com/maff0000/CGPT-INVESTMENT/blob/330c006522effd37ca435f754659f075564d6f72/research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) and [private PR #6 corrective instructions](https://github.com/maff0000/paper-bots/pull/6#issuecomment-6683142810). **The earlier 'CURRENT/PROPOSED' builder notices below are historical pre-audit snapshots; do not accept or merge PRs #6/#10.** M4 remains ACCEPTED. G0 OPEN, provider rights UNVERIFIED, FMP three historical calls only, stop-dependent M/T HOLD; native messaging/host ACL remain UNVERIFIED; no live/vendor/broker calls, scheduling or orders.

> **CURRENT — Increment A, 6 Nov 2026. Proposed. Not accepted. Not merged.** Private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` is parent-verified OPEN, draft false, `merged` false, `merged_at` null, mergeable clean. Parent of that commit, and unchanged paper-bots main, is `ff13c49ce2535992c7216f5742946b33bd805e53`. [REVIEW-M5-TRANSPORT-001](../research/reviews/2026-11-06-wo-paper-005-offline-transport-packet.md) is pinned to the head of `cursor/wo-paper-005-transport-packet-f3e8` and does not contain that public commit's SHA. Builder 132/132 is not Architect acceptance. This increment does not authenticate native senders and does not implement a host access-control list. [REVIEW-M4-ACCEPT-001](../research/reviews/2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains accepted history for the offline in-process adapter only. Earlier HOLDs of `553ec517455ce6ef797b049e65ec61389daa20da` and `f4371c599fb1c45e28c403549090e92fd825ce67` remain valid only for those older exact heads.

**Status:** PROPOSED for Architect review. Not accepted. Not merged.  
**Authoritative packet:** [REVIEW-M5-TRANSPORT-001](../research/reviews/2026-11-06-wo-paper-005-offline-transport-packet.md)  
**Parent PID:** [PID-EQUITY-PAPER-001](../docs/pid-equity-paper-system.md)  
**Private pull request:** [paper-bots #6](https://github.com/maff0000/paper-bots/pull/6)  
**Private work order path, not copied here:** `docs/work-orders/WO-PAPER-005-native-transport.md`  
**Accepted predecessor:** [WO-PAPER-004](WO-PAPER-004-native-ledger.md), paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`

## Parent-verified heads

| Item | Value |
|---|---|
| Public `origin/main` before this note | `1fc4491a095d914b855a2653cb8b753c7fbc3f13` |
| Parents of that public main | `b0c8f55109fcc92d8f55ec7b593c696b9887475d`, `8d3c32ebd34c94d182833e7fcb865865bf62e1e5` |
| Private branch | `cursor/wo-paper-005-native-transport-2076` |
| Private head under review | `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` |
| Parent of that commit / unchanged paper-bots main | `ff13c49ce2535992c7216f5742946b33bd805e53` |
| Private state | OPEN, draft false, `merged` false, `merged_at` null, mergeable clean |
| Diff versus accepted main | 1 commit, 23 files, +1743 / −3 |
| Private commit message | Add an offline spool in front of the accepted native writer. |

Merged public [PR #9](https://github.com/maff0000/CGPT-INVESTMENT/pull/9) is the closed WO-PAPER-004 governance record. This note does not reopen it.

## Discovery findings

Re-read on 6 Nov 2026 from the public pages. No probe was sent.

- [Security FAQ](https://docs.x.ai/grok-bot/security-faq): isolation is per Cursor user. Bots of one user share one computer. A Bot has no identity of its own. A workload that needs its own computer and credential set is given its own Cursor user.
- [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps): files, sign-ins, and command-line credentials are shared. Screens are separate work surfaces and are not security boundaries.
- [Security](https://cursor.com/docs/grok-bot/security): a Bot has no identity or credentials of its own and acts as the signed-in member.
- [Bots](https://docs.x.ai/grok-bot/bots): separate names, conversations, and memory still share the computer. Files and sign-ins are not isolated per Bot.
- [Chat and collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration): there is no switch that disables bot-to-bot messaging.
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises): one user's Bots share one computer, files, logins, and permitted connectors. The documented separate-computer path is a separate Cursor user.

A shared mailbox, an HMAC file, or an in-process role check is rejected as theatre in private ADR 0013. Those mechanisms are not built here.

## Increment A — demonstrated on the private head

Offline spool in front of accepted `paperbots.native_ingest`. Submission is an untrusted envelope plus a separate attestation sidecar (`attested_native_bot_id`, `attestation_source`, `submission_id`, envelope file SHA-256). The envelope cannot mint the sidecar. Missing, mismatched, or non-allowlisted attestation is fail-closed and does not write.

Receipts: `accepted` (event id and hash), `duplicate`, `conflict`, `validation`, `permission`, `attestation_missing`, `transport_error`. Exclusive lock. Crash or outage drain does not double-append. A crash after commit and before the receipt is `duplicate`, because the receipt follows ledger state. Drain order is lexical `submission_id`. One ledger transaction per submission.

Only `synthetic_fixture` is accepted. `parent_platform_metadata` is named and refused, so a source label cannot be read as platform proof.

The NEO snapshot reader has no write method. The snapshot hash detects truncation and is not a signature. The reader does not stop another same-user Bot from opening the ledger file.

## Increments B and C — gated

| Increment | What it would be | State |
|---|---|---|
| B | Parent-mediated live native messaging | Not implemented |
| C | Dedicated writer/NEO principal. Official recommendation: a separate Cursor user | Not implemented |

Neither increment is this pull request. No bot message was sent. No host principal was changed.

## Unchanged decision semantics

Replay, quality type guard, role binding, causal parents, and `note` as non-semantic stay as accepted in WO-PAPER-004. Synthetic path remains `NO_ORDER`, with `order_created` false and `is_fill` false. Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged.

## Private names

Names only. Fixture bodies are not copied. The 23-file diff includes files inside the fixture directory.

- `src/paperbots/native_transport.py`
- `src/paperbots/errors.py`
- `tests/test_native_transport.py`
- `docs/adr/0013-offline-native-transport.md`
- `docs/work-orders/WO-PAPER-005-native-transport.md`
- `fixtures/native/wo005_transport/`
- Pointer updates: `docs/adr/0010-native-role-contract.md`, `docs/adr/0012-native-ledger-ingest.md`, `docs/work-orders/WO-PAPER-004-native-ledger.md`, `README.md`, `RUNBOOK.md`

## Builder tests

Parent-confirmed from detached worktree `/tmp/wo005-final` at `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`. Command `PYTHONPATH=src python3.X -m unittest discover -s tests -v`. Not an Architect run.

- Python 3.9.25: exit 0, stdout 0 bytes, wall 1.733s, stderr `Ran 132 tests in 1.412s` / OK.
- Python 3.12.3: exit 0, stdout 0 bytes, wall 1.436s, stderr `Ran 132 tests in 1.286s` / OK.

The 132 include the previously accepted 117. Builder 132/132 is not Architect acceptance.

## Exclusions

No merge. No acceptance of the private head by this note. No live native messaging. No dedicated writer principal. No host access-control list. No bot message. No host-principal change. No scheduler. No live order. No broker or account read. No vendor call. No new entry, exit, stop, or risk parameter. No trade-policy approval.

G0 stays OPEN. Provider rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. No fourth call. Stop-dependent M/T stays HOLD.

## Remaining limitations

This increment does not authenticate native senders and does not implement a host access-control list. The snapshot hash is a truncation check, not a signature. Another Bot of the same user can still open the ledger file. Increments B and C remain gated. Paper-bots main stays `ff13c49ce2535992c7216f5742946b33bd805e53` until an Architect decision and a later reviewed merge.

## Requested next step

Architect independent re-audit of exact private head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`, then ACCEPT or HOLD on that head. This note is the handoff. It is not the decision.
