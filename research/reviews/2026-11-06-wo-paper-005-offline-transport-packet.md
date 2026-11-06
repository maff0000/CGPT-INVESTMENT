# WO-PAPER-005 — offline native transport, Increment A

**ID:** REVIEW-M5-TRANSPORT-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for an open private increment.  
**Disposition requested:** Architect **ACCEPT or HOLD** of exact private head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`.  
**This packet does not accept that head.** It does not merge private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) or this public pull request. Builder **132/132 is not Architect acceptance**. This increment does not authenticate native senders and does not implement a host access-control list.

Accepted history stays accepted. [REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) records the independent acceptance of private paper-bots PR #5 head `541f3f175da8ec684f942dea767a1352cf5df0fb` and the normal merge to paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`. That acceptance is the offline in-process synthetic adapter only. [REVIEW-M3-ACCEPT-001](2026-11-06-m3-70a673-independent-acceptance.md) stays the acceptance of private PR #4 head `70a673f973bd52155d495f6873eb417374f4948b`, paper-bots main at that time `b2cb75867d2408a0018333213a0dd2cfb91ac670`. This packet does not reopen either acceptance.

[REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Those HOLDs are valid only for those older exact heads. Neither HOLD file is edited here. Merged public [PR #9](https://github.com/maff0000/CGPT-INVESTMENT/pull/9) is closed history and is not this work.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-005-transport-packet-f3e8` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `git fetch origin main` returned `1fc4491a095d914b855a2653cb8b753c7fbc3f13`, message `Merge WO-PAPER-004 independent acceptance and M4 governance closure`, parents `b0c8f55109fcc92d8f55ec7b593c696b9887475d` and `8d3c32ebd34c94d182833e7fcb865865bf62e1e5`. That SHA is the parent of this public commit. Public PR #9 is MERGED (`mergedAt` 2026-11-06T10:10:46Z, head `8d3c32ebd34c94d182833e7fcb865865bf62e1e5`) |
| Re-read by this public session, 2026-11-06 | The six public platform pages linked below. No probe was sent |
| Parent-verified private read-back, 2026-11-06 Europe/London | Private PR #6 state, head, parent, base, branch, diff size, named paths, Increment A behaviour, and the builder test transcript at detached worktree `/tmp/wo005-final` |
| Not claimed here | Architect acceptance of `d57f2e32`, a merge, authenticated native senders, a host access-control list, a changed host principal, a bot message, vendor rights, or a fourth FMP call |

This public session did not open `maff0000/paper-bots` and did not copy private source, fixtures, raw vendor data, or credentials. Private facts below are the parent read-back.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main` before this write, and parent of this public commit | `1fc4491a095d914b855a2653cb8b753c7fbc3f13` |
| Parents of that public main | `b0c8f55109fcc92d8f55ec7b593c696b9887475d`, `8d3c32ebd34c94d182833e7fcb865865bf62e1e5` |
| Private pull request | [paper-bots #6](https://github.com/maff0000/paper-bots/pull/6) |
| Private title | WO-PAPER-005: offline spool in front of the accepted native writer |
| Private branch | `cursor/wo-paper-005-native-transport-2076` |
| Private head under review | `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` |
| Parent of that private commit | `ff13c49ce2535992c7216f5742946b33bd805e53` |
| Private commit message | Add an offline spool in front of the accepted native writer. |
| Unchanged paper-bots main and PR base | `ff13c49ce2535992c7216f5742946b33bd805e53` (WO-PAPER-004 merge; parents `b2cb75867d2408a0018333213a0dd2cfb91ac670` and `541f3f175da8ec684f942dea767a1352cf5df0fb`) |
| Private state | OPEN, draft false, `merged` false, `merged_at` null, mergeable clean |
| Diff versus accepted paper-bots main | 1 commit, 23 files, +1743 / −3 |
| Public branch for this packet | `cursor/wo-paper-005-transport-packet-f3e8` |
| Public note | [WO-PAPER-005](../../work-orders/WO-PAPER-005-native-transport.md) |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |

## Official platform findings, re-read 2026-11-06

This session re-read the public pages. The findings below are what those pages support. They are not a new architecture approval.

| Source | What it supports |
|---|---|
| [Security FAQ](https://docs.x.ai/grok-bot/security-faq) | Isolation is per Cursor user. Within one user, every Bot shares that computer. A login or file on it is available to every Bot that user runs. A Bot has no identity of its own. A workload that needs its own computer and credential set is given its own Cursor user |
| [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) | One computer is shared by all of a user's Bots: files, browser sessions, and command-line credentials. The computer is assigned to the user account. Each Bot can have its own screen. Screens are separate work surfaces and are not separate security boundaries |
| [Security](https://cursor.com/docs/grok-bot/security) | A Bot has no identity or credentials of its own. Bots act as the signed-in member. Per-user isolation sits beside source permissions, approvals, and team connector policy |
| [Create and manage Bots](https://docs.x.ai/grok-bot/bots) | Bots have separate names, conversations, and memory, and they share the computer. Files and sign-ins on that computer are not isolated per Bot |
| [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) | Bots message each other to hand off work. There is no switch that disables bot-to-bot messaging. Instructions govern it |
| [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) | Within one user, all of that user's Bots share one computer. Bots isolate personalities and workspaces, not compute. A permitted connector is available to every Bot that member runs. A separate computer and credential set means a separate Cursor user |

## Increment A — what the private head demonstrates

Parent-read behaviour, not an Architect confirmation. Increment A sits an offline spool in front of the accepted `paperbots.native_ingest` writer.

A submission is an untrusted envelope plus a separate attestation sidecar. The sidecar carries `attested_native_bot_id`, `attestation_source`, `submission_id`, and the envelope file SHA-256. The envelope cannot mint the sidecar. A missing sidecar, a mismatched attestation, a non-allowlisted attested id, or a contradictory envelope identity claim is fail-closed and does not write.

Receipts are `accepted` (event id and hash), `duplicate`, `conflict`, `validation`, `permission`, `attestation_missing`, and `transport_error`. The spool takes an exclusive lock. Drain after a crash or outage does not double-append. A crash after commit and before the receipt is acknowledged as `duplicate`, because the receipt follows ledger state. Drain order is lexical `submission_id`. One ledger transaction is used per submission.

Only `synthetic_fixture` is an accepted attestation source. `parent_platform_metadata` is named and refused, so a source label cannot be read as platform proof.

## Increments B and C — gated, not this pull request

| Increment | Scope | State |
|---|---|---|
| A | Offline spool in front of the accepted in-process writer, with a separate attestation sidecar | Proposed on private PR #6. Not accepted |
| B | Parent-mediated live native messaging | Gated. Not implemented |
| C | A dedicated writer/NEO principal. The official recommendation for a separate computer and credential set is a separate Cursor user | Gated. Not implemented |

No bot message was sent. No host principal was changed.

## NEO snapshot reader

The parent-read NEO path is an immutable snapshot plus a content hash. `NeoEvidenceReader` reconstructs the chain and has no append, ingest, or commit method. The snapshot hash detects truncation. It is not a signature. The reader does not stop another Bot of the same user from opening the ledger file.

## Rejected as theatre

Private ADR 0013, parent-read and not copied here, rejects a shared mailbox, an HMAC file, or an in-process role check as a security boundary. Those mechanisms are not this increment. The platform findings above are why they are rejected: same-user Bots share the computer, files, logins, and connectors, and a Bot has no identity of its own.

## Unchanged accepted decision semantics

Accepted WO-PAPER-004 decision semantics stay in `native_ingest`: replay integrity, the quality type guard, role binding, causal parents, `note` as non-semantic, and synthetic HOLD / `NO_ORDER` with `order_created` false and `is_fill` false. The frozen QARP-ROTATION-001 v1.0.0 file SHA-256 above is unchanged. Trade, stop, and entry authority remain NONE.

## Private names

Names only. The parent-verified diff is 23 files. This list names the paths and the fixture directory. Fixture bodies are not copied.

1. `src/paperbots/native_transport.py`
2. `src/paperbots/errors.py`
3. `tests/test_native_transport.py`
4. `docs/adr/0013-offline-native-transport.md`
5. `docs/work-orders/WO-PAPER-005-native-transport.md`
6. `fixtures/native/wo005_transport/` (synthetic envelope and sidecar pairs; the sidecar is a separate file)
7. Pointer-only updates: `docs/adr/0010-native-role-contract.md`, `docs/adr/0012-native-ledger-ingest.md`, `docs/work-orders/WO-PAPER-004-native-ledger.md`, `README.md`, `RUNBOOK.md`

## Tests

Parent-confirmed builder transcript. Not an Architect run. Detached worktree `/tmp/wo005-final` at `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`, parent `ff13c49ce2535992c7216f5742946b33bd805e53`. Command: `PYTHONPATH=src python3.X -m unittest discover -s tests -v`. Stdout 0 bytes on both.

| Interpreter | Exit | Wall | Stderr |
|---|---|---|---|
| Python 3.9.25 (`/home/ubuntu/.local/bin/python3.9`, uv CPython build) | 0 | 1.733s | `Ran 132 tests in 1.412s` / OK |
| Python 3.12.3 (`/usr/bin/python3.12`) | 0 | 1.436s | `Ran 132 tests in 1.286s` / OK |

The 132 include the previously accepted 117. **Builder 132/132 is not Architect acceptance.**

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- No vendor call, broker or account read, credential, raw bar, or private fixture body is added to this public repository.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, or trade-policy approval is granted.

## Limitations

- Increment A is an offline spool in front of the accepted in-process writer.
- This increment does not authenticate native senders and does not implement a host access-control list.
- The snapshot hash detects truncation and is not a signature.
- The NEO reader does not stop another same-user Bot from opening the ledger file.
- Increments B and C are gated and are not implemented.
- No bot message was sent. No host principal was changed.
- Paper-bots main is unchanged at `ff13c49ce2535992c7216f5742946b33bd805e53`. Private PR #6 is open.

## Restrictions

This packet authorises none of the following:

- acceptance of `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`
- merge of private PR #6 or of this public pull request
- live native messaging, a dedicated writer principal, or a host access-control list
- live orders, broker writes, or account reads
- vendor calls
- a scheduler or activation
- new entry, exit, stop, or risk parameters
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect re-audit of exact private head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`, then an **ACCEPT** or **HOLD** recorded against that SHA. Until that independent review exists, Increment A stays proposed. Passing builder tests, an open private pull request, and this public packet are review inputs. They are not the decision.

Rollback of an unaccepted increment is to leave paper-bots main at `ff13c49ce2535992c7216f5742946b33bd805e53` and public main at `1fc4491a095d914b855a2653cb8b753c7fbc3f13` until a later reviewed merge. This file does not perform either merge.
