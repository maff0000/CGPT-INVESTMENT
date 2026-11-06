# WO-PAPER-007 — native NEO communication (public note)

**Status:** Architect **ACCEPT** of exact private head `8b27454eb2485f8fc3897e60d316b4bb11e4a885`. Design only. That acceptance does not apply to any later commit. Private [paper-bots PR #10](https://github.com/maff0000/paper-bots/pull/10) is not yet merged. No native message is authorised.
**Acceptance record:** [REVIEW-M7-NEO-001](../research/reviews/2026-11-06-wo-paper-007-native-communication-acceptance.md)
**Predecessor:** [WO-PAPER-006](WO-PAPER-006-neo-decision-review.md). That file's historical ACCEPT and closure text is not rewritten. WO-PAPER-006 acceptance and closure remain [REVIEW-M6-NEO-003](../research/reviews/2026-11-06-wo-paper-006-neo-review-acceptance.md) and [REVIEW-M6-NEO-004](../research/reviews/2026-11-06-wo-paper-006-neo-review-closure.md).
**Private pull request:** [paper-bots #10](https://github.com/maff0000/paper-bots/pull/10), OPEN, not draft, not merged, on `cursor/wo-paper-007-native-neo-readiness-51cb`.
**Private work-order path, not copied here:** `docs/work-orders/WO-PAPER-007-native-neo-communication.md`

This public session did not open `maff0000/paper-bots`. The facts below are the parent's 6 November 2026 read-back, recorded in the acceptance record. This note does not copy the private work-order body, the private contract bodies, private Python, tests, fixtures, or schema catalog JSON. It does not record a prospective `merge_commit_sha`.

Public main at the time of this note is `7a61c57952e19c11bad67d0997d553939a030acd` (`Merge PR #13 — WO-PAPER-006 Architect acceptance and closure`). This note does not contain the SHA of the public commit that adds it.

## Accepted design

The Project Architect accepted the WO-PAPER-007 design at exact head `8b27454eb2485f8fc3897e60d316b4bb11e4a885` only. The commit message of that head is `Correct WO-PAPER-007 finding identity and append-only lifecycle.` Its parent `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53` is the earlier design commit (`Propose WO-PAPER-007 native NEO communication readiness.`). The correction addresses both previous HOLD findings against that earlier head. That earlier head remains historical. It is not the accepted SHA.

Compare of unchanged private main `28fe536e03ab8df1704d119b045158cc0a766f4f` to the accepted head: ahead 2, behind 0, 16 files, +765/−0. Documentation only. No `src/`, `tests/`, `fixtures/`, `examples/`, or `docs/schemas/` files. The correction commit alone is +121/−33 across five documentation files.

Every Architect acceptance criterion is PASS: nine individual finding IDs required; finding codes and supporting evidence validated; prepared request remains immutable; dispatch, acknowledgement and response are separate appends; replay and conflict handling specified; no historical row updates or deletes; claimed identity remains unauthenticated; no live message or trading authority; documentation-only scope.

Architect clarification for the next implementation work order, not a blocker to this design and not a change to this SHA: the implementation must use `(lifecycle_event, message_id)` as the unique lookup identity and compare the stored basis hash to distinguish replay from conflict.

## Exact accepted SHA

| Item | Value |
|---|---|
| Accepted private head | `8b27454eb2485f8fc3897e60d316b4bb11e4a885` |
| Parent | `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53` |
| Private main and PR base | `28fe536e03ab8df1704d119b045158cc0a766f4f` |
| Private PR | OPEN, not merged |
| Public main at this note | `7a61c57952e19c11bad67d0997d553939a030acd` |

## Accepted artefacts

Accepted, by name only. Bodies are not copied.

- WO-PAPER-007 design, private path `docs/work-orders/WO-PAPER-007-native-neo-communication.md`
- ADR 0017, private path `docs/adr/0017-native-message-provenance.md`
- `native-message-1`, private paths `docs/contracts/native-message-1.md` and `docs/contracts/native-message-1-schema.md`
- `native-review-response-1`
- The prepared, unsent T-Bot → NEO handoff, private path `docs/handoffs/2026-11-06-tbot-to-neo-wo007-PREPARED-NOT-SENT.md`
- The proposed append-only communication lifecycle
- The negative-test requirements

## Nine-finding-ID rule

A later native review must include all nine planted finding IDs, each with the matching code and evidence that supports that finding. Unique taxonomy codes are not completeness, because `REASONING_DOES_NOT_FOLLOW` and `MISSING_EVIDENCE` each cover two findings. A missing planted finding ID is `REJECT_HOLD` with reason `PLAYBOOK_INCOMPLETE`.

The nine IDs, already public from WO-PAPER-006 records, are `F-REASON-S-EARNINGS`, `F-REASON-S-MARGIN`, `F-MISSING-S-CONFIRMATION`, `F-BROKEN-M-CAUSAL`, `F-INCONSISTENT-M-RBOT`, `F-MISSING-M-SKEPTIC`, `F-HOLD-M-RBOT`, `F-MISSED-S-WO006B`, and `F-OUTCOME-M-MARK`.

## Append-only lifecycle

Prepared requests, authorised dispatches, acknowledgements, and responses are separate appends. A stored prepared row stays `PREPARED_NOT_SENT`. No historical row may be updated or replaced. SQL `UPDATE` and `DELETE` stay rejected. There is no second ledger.

## Provenance classification

Claimed sender identity stays a claim. Platform-attested identity stays `NOT_DOCUMENTED`. Authenticated sender stays HOLD. `authenticates_sender` stays false. `parent_platform_metadata` stays `REFUSED`. Status of this increment remains `PREPARED_NOT_SENT`. Sender T-Bot `81d8cf38-188e-4592-b08d-b59d6e461e83`. Recipient NEO `e1e372c8-20e9-45a6-856f-4eabdf018308`. No native message was sent.

## Restrictions

This acceptance does not authorise sending the native message, implementing or activating live transport under this design-only pull request, treating a claimed sender as authenticated, changing QARP, risk limits, trading authority, or historical evidence, or deploying Increment C isolation.

QARP-ROTATION-001 v1.0.0 file SHA-256 remains `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. Ruleset digest remains `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. The planted session, playbook, v0.3 catalog, and `decision-evidence-1` contract are unchanged. Parent-verified request-body SHA-256 remains `a310fb2a49ace2db1e42f204de210e915187fdb26d6d2ccc67b345489b5d3b2c`. G0 remains OPEN. Provider rights remain UNVERIFIED. Stop-dependent M/T pathways remain HOLD.

Builder-reported Python 3.12.3 `Ran 162 tests`, `OK`, is the unchanged WO-PAPER-006 suite. It is not Architect acceptance and it is not proof of native authentication. The Architect reviewed the documentation correction and did not independently execute Python.

## What this note does not do

Private PR #10 is not yet merged. This note does not merge it. It does not send a native message. It does not implement transport. Parent will independently read the public acceptance commit, then merge the private pull request using an ordinary merge commit pinned to `8b27454eb2485f8fc3897e60d316b4bb11e4a885`. This note does not name that future merge SHA.
