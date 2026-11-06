# WO-PAPER-008 — offline native message (public note)

> **CURRENT — 6 November 2026: WO-PAPER-008 closure record. This public pull request is not merged.** [REVIEW-M8-NEO-003](../research/reviews/2026-11-06-wo-paper-008-offline-native-message-closure.md) is that closure record. Public main at the start of this write is `1a25ee53bd9d0725ee654d7aa71556c03c466a5e`. Public [PR #15](https://github.com/maff0000/CGPT-INVESTMENT/pull/15) is merged as `05e87193e3d69d7b0e832219caf6b0f7dd962f4c`. Public [PR #16](https://github.com/maff0000/CGPT-INVESTMENT/pull/16) is merged as `1a25ee53bd9d0725ee654d7aa71556c03c466a5e` (that SHA is also the current public main). Private [paper-bots PR #12](https://github.com/maff0000/paper-bots/pull/12) is merged as `09fbdccba969de7ea96f727a528146f1ac37d3fa` (that SHA is also the current private main). [REVIEW-M8-NEO-001](../research/reviews/2026-11-06-wo-paper-008-offline-implementation-acceptance.md) remains the work-order ACCEPT of `705477daf2bced29e6dbaae11c186dd12c3e1206`. [REVIEW-M8-NEO-002](../research/reviews/2026-11-06-wo-paper-008-implementation-head-acceptance.md) remains the implementation ACCEPT of `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b`. No native message was sent. This write is not a merge instruction. The status line and the historical wording below that say private PR #11 stays open are the pre-closure record.

**Status:** Architect **ACCEPT** of exact private head `705477daf2bced29e6dbaae11c186dd12c3e1206`. That acceptance does not apply to any later commit. The accepted head is the documentation-only work order. It is not an implementation. Private [paper-bots PR #11](https://github.com/maff0000/paper-bots/pull/11) stays open and is not merged by this note. This public note is not a merge instruction.
**Acceptance record:** [REVIEW-M8-NEO-001](../research/reviews/2026-11-06-wo-paper-008-offline-implementation-acceptance.md)
**Predecessor:** [WO-PAPER-007](WO-PAPER-007-native-neo-communication.md). That file's historical ACCEPT and closure text is not rewritten. A successor pointer is the only addition. WO-PAPER-007 acceptance and closure remain [REVIEW-M7-NEO-001](../research/reviews/2026-11-06-wo-paper-007-native-communication-acceptance.md) and [REVIEW-M7-NEO-002](../research/reviews/2026-11-06-wo-paper-007-native-communication-closure.md).
**Private pull request:** [paper-bots #11](https://github.com/maff0000/paper-bots/pull/11), OPEN, not draft, not merged, `mergeable` true, `mergeable_state` clean, on `cursor/wo-paper-008-offline-native-message-3e87`.
**Private work-order path, not copied here:** `docs/work-orders/WO-PAPER-008-offline-native-message.md`

This public session did not open `maff0000/paper-bots`. The facts below are the parent's 6 November 2026 (Europe/London) read-back, recorded in the acceptance record. This note does not copy the private work-order body, private Python, tests, fixtures, or schema catalog JSON. It does not record a prospective `merge_commit_sha`. It does not invent a private merge SHA.

Public main at the time of this note is `573920e8a4deedb898917b41223fa6710a253695` (`Merge PR #14 — WO-PAPER-007 Architect acceptance and closure`; parents `7a61c57952e19c11bad67d0997d553939a030acd` and `8ff348e01786de44925a27fc55e681a2eaf8b039`). This note does not contain the SHA of the public commit that adds it.

## Accepted work order

The Project Architect accepted WO-PAPER-008 at exact head `705477daf2bced29e6dbaae11c186dd12c3e1206` only. The commit message of that head is `Propose WO-PAPER-008 offline native-message work order.` Its parent is unchanged private main `d2c7fe9a4df8590488202e63dc3820480fd82546` (`Merge PR #10 — WO-PAPER-007 native NEO communication readiness`; parents `28fe536e03ab8df1704d119b045158cc0a766f4f` and accepted WO-PAPER-007 design `8b27454eb2485f8fc3897e60d316b4bb11e4a885`).

Compare of that base to the accepted head: ahead 1, behind 0, one commit, 5 files, +352/−0. Documentation only. No `src/`, `tests/`, `fixtures/`, `examples/`, or `docs/schemas/` files. The five files, named only, are `README.md` +4/−0, `RUNBOOK.md` +4/−0, `docs/roadmap/bot-self-improvement.md` +4/−0, a successor pointer only on `docs/work-orders/WO-PAPER-007-native-neo-communication.md` +4/−0, and added `docs/work-orders/WO-PAPER-008-offline-native-message.md` +336/−0.

The private pull-request title remains `WO-PAPER-008 offline native-message work order (proposed, not an implementation, not accepted)`. That title is the parent read-back. This note records the Architect ACCEPT of that exact head and does not edit the private repository.

Every Architect-confirmed finding is PASS: private PR #11 remains open and unmerged; the base is `d2c7fe9a4df8590488202e63dc3820480fd82546`; the proposal changes five documentation files only; parent WO-PAPER-007 and its accepted contracts are correctly referenced; all nine planted findings are required individually; the idempotency lookup uses `(lifecycle_event, message_id)`, with the stored basis hash determining replay or conflict; no implementation, live transport, or handoff is included.

## Exact accepted SHA

| Item | Value |
|---|---|
| Accepted private head | `705477daf2bced29e6dbaae11c186dd12c3e1206` |
| Parent | `d2c7fe9a4df8590488202e63dc3820480fd82546` |
| Private main and PR base | `d2c7fe9a4df8590488202e63dc3820480fd82546` |
| Private PR | OPEN, not merged |
| Public main at this note | `573920e8a4deedb898917b41223fa6710a253695` |

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

1. Acknowledgement storage: only bounded, explicitly synthetic acknowledgement fixtures are authorised. Arbitrary future live-tool acknowledgement bytes are outside this work order. Their shape, retention, and sanitisation require separate review.
2. Ledger idempotency: the existing ledger compares more than the proposed basis hash. The new recorder must enforce the accepted replay/conflict semantics without altering the established ledger, creating a second insertion route, or updating existing rows.

## What the acceptance authorises

The bounded, offline implementation of the message parser, evidence resolver, append-only recorder, and associated tests, on a dedicated implementation branch, subject to the exact-base and scope checks in the private work order. This public note does not perform that implementation. It does not paste private module bodies or test code.

## What the acceptance does not authorise

- Merging private PR #11
- Merging any later implementation pull request
- Sending the native message or the prepared T-Bot → NEO handoff
- Implementing or activating live transport
- Treating a claimed sender as authenticated
- Adding the deferred offline `check` command
- Changing QARP-ROTATION-001 v1.0.0, risk limits, trading authority, or historical evidence
- Deploying Increment C isolation
- Introducing a paid model API or starting the later v2 port

## Restrictions

Prepared status stays `PREPARED_NOT_SENT`. `authenticates_sender` remains false. `parent_platform_metadata` remains `REFUSED`. G0 remains OPEN. Provider rights remain UNVERIFIED. Stop-dependent M/T pathways remain HOLD. QARP-ROTATION-001 v1.0.0 is unchanged: file SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`; ruleset digest `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. No paid model API, live trading, strategy promotion, or Increment C deployment. No market-data calls, broker interaction, new accounts, or second ledger. Do not widen `native-ledger-1` or alter the v0.3 catalog.

The nine planted finding IDs remain `F-REASON-S-EARNINGS`, `F-REASON-S-MARGIN`, `F-MISSING-S-CONFIRMATION`, `F-BROKEN-M-CAUSAL`, `F-INCONSISTENT-M-RBOT`, `F-MISSING-M-SKEPTIC`, `F-HOLD-M-RBOT`, `F-MISSED-S-WO006B`, and `F-OUTCOME-M-MARK`. Unique taxonomy codes are not completeness.

## What this note does not do

Private PR #11 stays open and unmerged. This note does not merge it. It does not name a future merge SHA. It does not send a native message. It does not implement transport, the parser, the resolver, the recorder, or the deferred offline `check` command. Historical REVIEW-M7, REVIEW-M6, and REVIEW-M5 files stay as written.
