# REVIEW-M8-NEO-001 — WO-PAPER-008 Architect acceptance

**ID:** REVIEW-M8-NEO-001
**Date:** 6 November 2026 (Europe/London)
**Architect decision:** **ACCEPT** exact private head `705477daf2bced29e6dbaae11c186dd12c3e1206`.
**That acceptance does not apply to any later commit.**
**Not merged. Not an implementation.** Private [paper-bots PR #11](https://github.com/maff0000/paper-bots/pull/11) stays open. This record does not merge that pull request. This public pull request is not a merge instruction and does not merge itself. It does not invent a merge SHA, and it does not quote a prospective `merge_commit_sha`. It does not implement a parser, resolver, recorder, or tests.

Public main at the time of this write is `573920e8a4deedb898917b41223fa6710a253695`. Message: `Merge PR #14 — WO-PAPER-007 Architect acceptance and closure`. Parents: `7a61c57952e19c11bad67d0997d553939a030acd` and `8ff348e01786de44925a27fc55e681a2eaf8b039`. That SHA is already the merge of public PR #14. It is the parent of the public commit that adds this file.

This file does not contain the SHA of the public commit that adds it. It is pinned to the head of `cursor/wo-paper-008-architect-accept-792a` after that commit is pushed.

This public session did not open `maff0000/paper-bots`. Private facts below are the parent's 6 November 2026 (Europe/London) read-back. No private Python, tests, fixtures, schema catalog JSON, or full private contract or work-order bodies are copied. Named private paths and SHAs are recorded. Historical REVIEW-M5, REVIEW-M6, and REVIEW-M7 files are not rewritten. [WO-PAPER-007](../../work-orders/WO-PAPER-007-native-neo-communication.md) receives a successor pointer only.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `573920e8a4deedb898917b41223fa6710a253695`, message `Merge PR #14 — WO-PAPER-007 Architect acceptance and closure`, parents `7a61c57952e19c11bad67d0997d553939a030acd` and `8ff348e01786de44925a27fc55e681a2eaf8b039`. No existing public WO-PAPER-008 pull request. Merged public PRs #10, #11, #12, #13, and #14 are not reused |
| Parent-supplied read-back, 6 November 2026, Europe/London | Private PR #11 state, exact head, ancestry, documentation-only diff, and the Architect acceptance itself |
| Not claimed here | A merge of either pull request, a merge SHA, a prospective `merge_commit_sha`, acceptance of any commit after `705477daf2bced29e6dbaae11c186dd12c3e1206`, an implementation of the parser, resolver, recorder, or tests, a sent native message, live transport, sender authentication, the deferred offline `check` command, a QARP or risk-limit change, a change to historical evidence, Increment C deployment, a paid model API, a later v2 port, a change of G0, verified provider rights, or release of stop-dependent M/T |

## Parent-verified private state

| Item | Value |
|---|---|
| Private pull request | [paper-bots #11](https://github.com/maff0000/paper-bots/pull/11) |
| Title | `WO-PAPER-008 offline native-message work order (proposed, not an implementation, not accepted)` |
| State | OPEN, not draft, not merged, `mergeable` true, `mergeable_state` clean |
| Branch | `cursor/wo-paper-008-offline-native-message-3e87` |
| Accepted head, and the only SHA this acceptance covers | `705477daf2bced29e6dbaae11c186dd12c3e1206` |
| Parent of that commit | `d2c7fe9a4df8590488202e63dc3820480fd82546` |
| Accepted-head commit message | `Propose WO-PAPER-008 offline native-message work order.` |
| Private main and PR base, unchanged | `d2c7fe9a4df8590488202e63dc3820480fd82546` |
| Private main message | `Merge PR #10 — WO-PAPER-007 native NEO communication readiness` |
| Private main parents | `28fe536e03ab8df1704d119b045158cc0a766f4f` and accepted WO-PAPER-007 design `8b27454eb2485f8fc3897e60d316b4bb11e4a885` |
| Compare `d2c7fe9a...705477da` | status ahead, ahead 1, behind 0, total_commits 1, 5 files, +352/−0 |
| Scope of that compare | Documentation only. No `src/`, `tests/`, `fixtures/`, `examples/`, or `docs/schemas/` files |
| Files, named only | `README.md` +4/−0; `RUNBOOK.md` +4/−0; `docs/roadmap/bot-self-improvement.md` +4/−0; successor pointer only on `docs/work-orders/WO-PAPER-007-native-neo-communication.md` +4/−0; added `docs/work-orders/WO-PAPER-008-offline-native-message.md` +336/−0 |
| Prospective `merge_commit_sha` | If GitHub shows one on the open pull request, it is not a merge and is not recorded here |

The private title still says the work order was proposed and not accepted. That title is the parent read-back of the open pull request. The Architect decision in this file is the acceptance of that exact head. This file does not edit `maff0000/paper-bots`.

## Architect-confirmed findings

The Project Architect independently inspected the work order, its GitHub commit, and the relevant existing ledger and schema-validation code, and ACCEPTED WO-PAPER-008 at exact private head `705477daf2bced29e6dbaae11c186dd12c3e1206`. Every finding below is PASS. The acceptance is final for that SHA only.

| Finding | Result |
|---|---|
| Private PR #11 remains open and unmerged | PASS |
| Base is `d2c7fe9a4df8590488202e63dc3820480fd82546` | PASS |
| The proposal changes five documentation files only | PASS |
| Parent WO-PAPER-007 and its accepted contracts are correctly referenced | PASS |
| All nine planted findings are required individually | PASS |
| The idempotency lookup uses `(lifecycle_event, message_id)`, with the stored basis hash determining replay or conflict | PASS |
| No implementation, live transport, or handoff is included | PASS |

## Section 12 decisions

All seven decisions are decided.

| # | Proposal | Decision |
|---|---|---|
| 1 | Synthetic dispatch and acknowledgement fixtures | ACCEPT |
| 2 | Opaque acknowledgement evidence | ACCEPT for bounded synthetic fixtures only |
| 3 | Local Git pin resolution | ACCEPT |
| 4 | Fixture response ID ending `0002` (`00700007-0007-4000-8000-000000000002`) | ACCEPT |
| 5 | Real send fields remain unset | ACCEPT |
| 6 | Catalog at `docs/schemas/native-message-1/` | ACCEPT |
| 7 | Narrow `schemautil.py` registration change | ACCEPT |

## Deferred offline check command

The optional offline `check` command is deferred. It is unnecessary for this implementation's acceptance and must not be added in the authorised implementation.

## Implementation boundaries

The Architect required particular attention to two boundaries. They bind the later implementation. They are not implemented by this public record.

1. Acknowledgement storage: only bounded, explicitly synthetic acknowledgement fixtures are authorised. Arbitrary future live-tool acknowledgement bytes are outside this work order. Their shape, retention, and sanitisation require separate review.
2. Ledger idempotency: the existing ledger compares more than the proposed basis hash. The new recorder must enforce the accepted replay/conflict semantics without altering the established ledger, creating a second insertion route, or updating existing rows.

The accepted lookup remains `(lifecycle_event, message_id)`. The stored basis hash determines replay or conflict. That comparison does not replace the rest of the existing ledger comparison.

## Authorised

This acceptance authorises the bounded, offline implementation of the message parser, evidence resolver, append-only recorder, and associated tests, on a dedicated implementation branch, subject to the exact-base and scope checks in the work order.

That implementation is not this public pull request. It is not private PR #11. Private PR #11 remains the documentation-only work order at `705477daf2bced29e6dbaae11c186dd12c3e1206`.

## Not authorised

- Merging private PR #11
- Merging any later implementation pull request
- Sending the native message or the prepared T-Bot → NEO handoff
- Implementing or activating live transport
- Treating a claimed sender as authenticated
- Adding the deferred offline `check` command
- Changing QARP-ROTATION-001 v1.0.0, risk limits, trading authority, or historical evidence
- Deploying Increment C isolation
- Introducing a paid model API or starting the later v2 port

## Restrictions that remain in force

- Prepared status stays `PREPARED_NOT_SENT`
- `authenticates_sender` remains false
- `parent_platform_metadata` remains `REFUSED`
- G0 remains OPEN
- Provider rights remain UNVERIFIED
- Stop-dependent M/T pathways remain HOLD
- QARP-ROTATION-001 v1.0.0 unchanged (file SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`; ruleset digest `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`)
- No paid model API, live trading, strategy promotion, or Increment C deployment
- No market-data calls, broker interaction, new accounts, or second ledger
- Do not widen `native-ledger-1` or alter the v0.3 catalog

## Nine finding IDs

The nine planted finding IDs remain: `F-REASON-S-EARNINGS`, `F-REASON-S-MARGIN`, `F-MISSING-S-CONFIRMATION`, `F-BROKEN-M-CAUSAL`, `F-INCONSISTENT-M-RBOT`, `F-MISSING-M-SKEPTIC`, `F-HOLD-M-RBOT`, `F-MISSED-S-WO006B`, and `F-OUTCOME-M-MARK`. Unique taxonomy codes are not completeness. The codes already published with those IDs stay in the historical WO-PAPER-006 and WO-PAPER-007 records. Those records are not rewritten.

## WO-PAPER-007 history

WO-PAPER-007 acceptance and closure remain historical: [REVIEW-M7-NEO-001](2026-11-06-wo-paper-007-native-communication-acceptance.md) and [REVIEW-M7-NEO-002](2026-11-06-wo-paper-007-native-communication-closure.md). Accepted design `8b27454eb2485f8fc3897e60d316b4bb11e4a885`. Private merge `d2c7fe9a4df8590488202e63dc3820480fd82546`. Public merge `573920e8a4deedb898917b41223fa6710a253695`. Those records are not rewritten. This acceptance does not invent a further private merge SHA.

Public work order for this acceptance: [WO-PAPER-008](../../work-orders/WO-PAPER-008-offline-native-message.md).

## What remains open

Private PR #11 stays open and unmerged. Private main stays `d2c7fe9a4df8590488202e63dc3820480fd82546`. Public main at this write stays `573920e8a4deedb898917b41223fa6710a253695`. This file names no future merge SHA. This record does not merge private PR #11. It does not merge this public pull request. It does not implement the message parser, evidence resolver, append-only recorder, or tests. It does not send a native message or the prepared handoff. It does not add the deferred offline `check` command.

The authorised next implementation, which this packet does not perform, is the bounded offline work named above, on a dedicated implementation branch, subject to the exact-base and scope checks in the work order.
