# REVIEW-M7-NEO-001 — WO-PAPER-007 Architect acceptance

> **DATED CLOSURE POINTER — 6 November 2026. This file is not rewritten.** Private [paper-bots PR #10](https://github.com/maff0000/paper-bots/pull/10) was later merged by an ordinary merge commit. The verified private merge SHA and private main are `d2c7fe9a4df8590488202e63dc3820480fd82546`. The accepted design remains `8b27454eb2485f8fc3897e60d316b4bb11e4a885`. [REVIEW-M7-NEO-002](2026-11-06-wo-paper-007-native-communication-closure.md) records that merge. The ACCEPT text below stays. Public PR #14 is not merged. No public merge SHA is recorded here.

**ID:** REVIEW-M7-NEO-001
**Date:** 6 November 2026 (Europe/London)
**Architect decision:** **ACCEPT** exact private head `8b27454eb2485f8fc3897e60d316b4bb11e4a885`.
**That acceptance does not apply to any later commit.**
**Not merged.** Private [paper-bots PR #10](https://github.com/maff0000/paper-bots/pull/10) stays open. This record does not merge that pull request and does not merge the public pull request that carries it. It does not invent a merge SHA, and it does not quote a prospective `merge_commit_sha`.

Public main at the time of this write is `7a61c57952e19c11bad67d0997d553939a030acd`. Message: `Merge PR #13 — WO-PAPER-006 Architect acceptance and closure`. Parents: `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` and `f3e0b230125cb3219b6ca31e83c50f7b5600ce01`. That SHA is already the merge of public PR #13. It is the parent of the public commit that adds this file.

This file does not contain the SHA of the public commit that adds it. It is pinned to the head of `cursor/wo-paper-007-architect-accept-b627` after that commit is pushed.

This public session did not open `maff0000/paper-bots`. Private facts below are the parent's 6 November 2026 (Europe/London) read-back. No private Python, tests, fixtures, schema catalog JSON, or full private contract or work-order bodies are copied. Named private paths and SHAs are recorded. Historical REVIEW-M5 and REVIEW-M6 files are not rewritten. [WO-PAPER-006](../../work-orders/WO-PAPER-006-neo-decision-review.md) receives a one-line successor pointer only.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `7a61c57952e19c11bad67d0997d553939a030acd`, message `Merge PR #13 — WO-PAPER-006 Architect acceptance and closure`, parents `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` and `f3e0b230125cb3219b6ca31e83c50f7b5600ce01`. No existing public WO-PAPER-007 pull request. Merged public PRs #10, #11, #12, and #13 are not reused |
| Parent-supplied read-back, 6 November 2026, Europe/London | Private PR #10 state, exact head, ancestry, documentation-only diff, the five correction files, GitHub check status, and the Architect acceptance itself |
| Not claimed here | A merge of either pull request, a merge SHA, a prospective `merge_commit_sha`, acceptance of any commit after `8b27454eb2485f8fc3897e60d316b4bb11e4a885`, acceptance of the earlier design head `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53`, an independent Python execution, a sent native message, live transport, sender authentication, a QARP or risk-limit change, a change to historical evidence, Increment C deployment, a change of G0, verified provider rights, or release of stop-dependent M/T |

## Parent-verified private state

| Item | Value |
|---|---|
| Private pull request | [paper-bots #10](https://github.com/maff0000/paper-bots/pull/10) |
| Title | `WO-PAPER-007 native NEO communication readiness (proposed, not accepted)` |
| State | OPEN, not draft, not merged, `mergeable` true, `mergeable_state` clean |
| Branch | `cursor/wo-paper-007-native-neo-readiness-51cb` |
| Accepted head, and the only SHA this acceptance covers | `8b27454eb2485f8fc3897e60d316b4bb11e4a885` |
| Parent of that commit | `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53` |
| Accepted-head commit message | `Correct WO-PAPER-007 finding identity and append-only lifecycle.` |
| First design commit | `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53`, parent `28fe536e03ab8df1704d119b045158cc0a766f4f`, message `Propose WO-PAPER-007 native NEO communication readiness.` |
| Earlier design head | `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53` remains historical. It is not the accepted SHA |
| Private main and PR base, unchanged | `28fe536e03ab8df1704d119b045158cc0a766f4f` |
| Private main message | `Merge PR #9 — WO-PAPER-006 synthetic NEO review` |
| Private main parents | `c0b9f540c09caec08fb87e77bf445d0e580f843e` and accepted WO-PAPER-006 implementation `4b3dac4c4137a5cb89a9587862e5fe25c464887b` |
| Private main tree | `0b6fdcf3a14976b611fa22b9c4b44759c857f02f` |
| Compare `28fe536e...8b27454` | status ahead, ahead 2, behind 0, total_commits 2, 16 files, +765/−0 |
| Scope of that compare | Documentation only. No `src/`, `tests/`, `fixtures/`, `examples/`, or `docs/schemas/` files |
| Correction commit alone | +121/−33 across five documentation files |
| Correction files, named only | `docs/work-orders/WO-PAPER-007-native-neo-communication.md`, `docs/contracts/native-message-1.md`, `docs/contracts/native-message-1-schema.md`, `docs/handoffs/2026-11-06-tbot-to-neo-wo007-PREPARED-NOT-SENT.md`, `docs/adr/0017-native-message-provenance.md` |
| GitHub check runs on `8b27454` | none (`total_count` 0) |
| Combined commit status | `pending` with zero statuses |
| Required reviews | No unresolved required reviews were visible |
| Prospective `merge_commit_sha` | If GitHub shows one on the open pull request, it is not a merge and is not recorded here |

## Acceptance criteria

The Project Architect independently reviewed the correction on paper-bots PR #10. Every criterion below is PASS. The acceptance is final for `8b27454eb2485f8fc3897e60d316b4bb11e4a885` only.

| Acceptance criterion | Result |
|---|---|
| Nine individual finding IDs required | PASS |
| Finding codes and supporting evidence validated | PASS |
| Prepared request remains immutable | PASS |
| Dispatch, acknowledgement and response are separate appends | PASS |
| Replay and conflict handling specified | PASS |
| No historical row updates or deletes | PASS |
| Claimed identity remains unauthenticated | PASS |
| No live message or trading authority | PASS |
| Documentation-only scope | PASS |

The correction addresses both previous HOLD findings against the earlier design head `e4aca6c3c97fd10b87a44f1c2b8bca033b316e53`. That earlier head remains historical. It is not the accepted SHA.

Architect clarification for the next implementation work order, not a blocker to accepting this design and not a change to this SHA: the implementation must use `(lifecycle_event, message_id)` as the unique lookup identity and compare the stored basis hash to distinguish replay from conflict.

## Accepted

- WO-PAPER-007 design
- ADR 0017
- `native-message-1`
- `native-review-response-1`
- The prepared, unsent T-Bot → NEO handoff
- The proposed append-only communication lifecycle
- The negative-test requirements

## Not authorised

- Sending the native message
- Implementing or activating live transport under this design-only pull request
- Treating a claimed sender as authenticated
- Changing QARP, risk limits, trading authority, or historical evidence
- Deploying Increment C isolation

## Nine finding IDs

A later native review must include all nine planted finding IDs, each with the matching code and evidence that supports that finding. Unique taxonomy codes are not completeness, because `REASONING_DOES_NOT_FOLLOW` and `MISSING_EVIDENCE` each cover two findings. A missing planted finding ID is `REJECT_HOLD` with reason `PLAYBOOK_INCOMPLETE`.

The nine IDs, already public from WO-PAPER-006 records, are:

| ID | Code already public from WO-PAPER-006 |
|---|---|
| `F-REASON-S-EARNINGS` | `REASONING_DOES_NOT_FOLLOW` |
| `F-REASON-S-MARGIN` | `REASONING_DOES_NOT_FOLLOW` |
| `F-MISSING-S-CONFIRMATION` | `MISSING_EVIDENCE` |
| `F-BROKEN-M-CAUSAL` | `BROKEN_CAUSAL_REFERENCE` |
| `F-INCONSISTENT-M-RBOT` | `CROSS_BOT_INCONSISTENCY` |
| `F-MISSING-M-SKEPTIC` | `MISSING_EVIDENCE` |
| `F-HOLD-M-RBOT` | `HOLD_VIOLATED` |
| `F-MISSED-S-WO006B` | `MISSED_OPPORTUNITY` |
| `F-OUTCOME-M-MARK` | `FAVOURABLE_OUTCOME_POOR_DECISION` |

## Append-only lifecycle

Prepared requests, authorised dispatches, acknowledgements, and responses are separate appends. A stored prepared row stays `PREPARED_NOT_SENT`. No historical row may be updated or replaced. SQL `UPDATE` and `DELETE` stay rejected. There is no second ledger.

## Provenance

Claimed sender identity stays a claim. Platform-attested identity stays `NOT_DOCUMENTED`. Authenticated sender stays HOLD. `authenticates_sender` stays false. `parent_platform_metadata` stays `REFUSED`. Status of this increment remains `PREPARED_NOT_SENT`. Sender T-Bot `81d8cf38-188e-4592-b08d-b59d6e461e83`. Recipient NEO `e1e372c8-20e9-45a6-856f-4eabdf018308`. No native message was sent.

## Unchanged pins

QARP-ROTATION-001 v1.0.0 file SHA-256 remains `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. Ruleset digest remains `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. The planted session, playbook, v0.3 catalog, and `decision-evidence-1` contract are unchanged. Parent-verified request-body SHA-256 remains `a310fb2a49ace2db1e42f204de210e915187fdb26d6d2ccc67b345489b5d3b2c`. G0 remains OPEN. Provider rights remain UNVERIFIED. Stop-dependent M/T pathways remain HOLD.

## Builder evidence

Builder-reported evidence, not independently executed by the Architect or by the parent: Python 3.12.3 `Ran 162 tests`, `OK`, from the unchanged suite. That count is the WO-PAPER-006 count. It is not Architect acceptance and it is not proof of native authentication. The Architect reviewed the documentation correction and did not independently execute Python. This public session did not run the suite.

## WO-PAPER-006 history

WO-PAPER-006 acceptance and closure remain historical: [REVIEW-M6-NEO-003](2026-11-06-wo-paper-006-neo-review-acceptance.md) and [REVIEW-M6-NEO-004](2026-11-06-wo-paper-006-neo-review-closure.md). Accepted implementation `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. Private merge `28fe536e03ab8df1704d119b045158cc0a766f4f`. Public merge `7a61c57952e19c11bad67d0997d553939a030acd`. Those records are not rewritten.

Public work order for this acceptance: [WO-PAPER-007](../../work-orders/WO-PAPER-007-native-neo-communication.md).

## What remains open

Private PR #10 stays open and unmerged. Private main stays `28fe536e03ab8df1704d119b045158cc0a766f4f`. Public main at this write stays `7a61c57952e19c11bad67d0997d553939a030acd`. This file names no future merge SHA. Parent will independently read the new public head, then merge private paper-bots PR #10 using an ordinary merge commit pinned to `8b27454eb2485f8fc3897e60d316b4bb11e4a885`. This record does not perform that merge. It does not send a native message. It does not implement transport.
