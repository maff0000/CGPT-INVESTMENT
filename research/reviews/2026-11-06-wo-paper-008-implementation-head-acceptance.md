# REVIEW-M8-NEO-002 — WO-PAPER-008 implementation-head acceptance

**ID:** REVIEW-M8-NEO-002
**Date:** 6 November 2026 (Europe/London)
**Work order:** WO-PAPER-008
**Architect decision:** **ACCEPT** exact private implementation head `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b`.
**That acceptance does not apply to any later commit.**
**Not merged. Not closure.** The acceptance is for offline synthetic implementation only. A passing simulation is not native authentication. No real native communication occurred. No native message was sent. Private [paper-bots PR #12](https://github.com/maff0000/paper-bots/pull/12) stays open. This record does not merge that pull request, private [paper-bots PR #11](https://github.com/maff0000/paper-bots/pull/11), or public [PR #15](https://github.com/maff0000/CGPT-INVESTMENT/pull/15). This public pull request is not a merge instruction and does not merge itself. It does not invent a merge SHA, and it does not quote a prospective `merge_commit_sha`. It does not implement a parser, resolver, recorder, or tests in this public repository.

Public main at the time of this write is `573920e8a4deedb898917b41223fa6710a253695`. Message: `Merge PR #14 — WO-PAPER-007 Architect acceptance and closure`. Parents: `7a61c57952e19c11bad67d0997d553939a030acd` and `8ff348e01786de44925a27fc55e681a2eaf8b039`. Tree: `f675456382e957365bc39738194b619a9c5522c0`. That SHA is already the merge of public PR #14. It is the parent of the public commit that adds this file. This branch is cut from that main. It is not cut from public PR #15.

This file does not contain the SHA of the public commit that adds it. It is pinned to the head of `cursor/wo-paper-008-implementation-accept-e03e` after that commit is pushed.

This public session did not open `maff0000/paper-bots`. Private facts below are the parent's 6 November 2026 (Europe/London) read-back. No private Python, tests, fixtures, schema catalog JSON, or full private contract or work-order bodies are copied. Named private paths and SHAs are recorded. Historical REVIEW-M5, REVIEW-M6, REVIEW-M7, and REVIEW-M8-NEO-001 text is not rewritten. [WO-PAPER-007](../../work-orders/WO-PAPER-007-native-neo-communication.md) receives a successor pointer only.

## Identifier

This public session confirmed the next identifier before writing. `origin/main` `573920e8a4deedb898917b41223fa6710a253695` contains no `REVIEW-M8-NEO` text. GitHub code search of that default branch for `REVIEW-M8-NEO-002` returned zero hits. The only remote head naming WO-PAPER-008 is `cursor/wo-paper-008-architect-accept-792a`, exact head `a9f5e9d301754dbf95095045d97fa5546431ed7a`, which is open public [PR #15](https://github.com/maff0000/CGPT-INVESTMENT/pull/15). The only WO-PAPER-008 review on that head is [REVIEW-M8-NEO-001](https://github.com/maff0000/CGPT-INVESTMENT/blob/a9f5e9d301754dbf95095045d97fa5546431ed7a/research/reviews/2026-11-06-wo-paper-008-offline-implementation-acceptance.md), the work-order ACCEPT of `705477daf2bced29e6dbaae11c186dd12c3e1206`. `REVIEW-M8-NEO-002` was unused. This file uses that identifier. It does not reuse REVIEW-M8-NEO-001. It does not edit, rename, or recreate that file or `work-orders/WO-PAPER-008-offline-native-message.md`. Those files exist on PR #15 and do not exist on this branch. A relative link to either file would be broken on this branch. Citations use the PR #15 URL and the blob URL at `a9f5e9d`.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `573920e8a4deedb898917b41223fa6710a253695`, message `Merge PR #14 — WO-PAPER-007 Architect acceptance and closure`, parents `7a61c57952e19c11bad67d0997d553939a030acd` and `8ff348e01786de44925a27fc55e681a2eaf8b039`, tree `f675456382e957365bc39738194b619a9c5522c0`. No `REVIEW-M8-NEO` text on that main. `REVIEW-M8-NEO-001` exists on open public PR #15 at `a9f5e9d301754dbf95095045d97fa5546431ed7a`. `REVIEW-M8-NEO-002` was unused. Merged public PRs #10, #11, #12, #13, and #14 are not reused. This branch is not public PR #15 |
| Parent-supplied read-back, 6 November 2026, Europe/London | Private PR #12 state, exact accepted implementation head, ancestry, the two-file correction diff, the two resolved defects, the fixture digest, builder-reported tests, and the Architect acceptance itself. Private PR #11 remains the unmerged work-order record |
| Not claimed here | A merge of any pull request, a merge SHA, a prospective `merge_commit_sha`, closure, acceptance of any commit after `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b`, withdrawal of the historical HOLDs as they apply to `9851d0e160a4dfe7aa2e29db23c92b0dc5e7b3fb` and `05930fc35e40ee009c80bcaa4ecdca88b35c02ba`, an independent Python execution by the Architect, a sent native message, live transport, sender authentication, the deferred offline `check` command, a QARP or risk-limit change, a change to historical evidence, Increment C deployment, a paid model API, a later v2 port, the new R-Bot optimisation task, a change of G0, verified provider rights, or release of stop-dependent M/T |

## Parent-verified private state

| Item | Value |
|---|---|
| Private implementation pull request | [paper-bots #12](https://github.com/maff0000/paper-bots/pull/12) |
| Title | `Implement WO-PAPER-008 offline native-message simulation` |
| State | OPEN, not draft, not merged, `mergeable` true, `mergeable_state` clean |
| Branch | `cursor/wo-paper-008-implementation-4e9a` |
| Accepted implementation head, and the only SHA this acceptance covers | `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b` |
| Parent of that commit | `05930fc35e40ee009c80bcaa4ecdca88b35c02ba` |
| Accepted-head commit message | `Require a consistent synthetic dispatch before an acknowledgement.` |
| Accepted-head body | `Reject delivery when that dispatch row is missing or its stored basis, identity, or disposition does not match the accepted synthetic dispatch. Pin the acknowledgement fixture SHA-256 and fail closed if those bytes change.` |
| Commit form | Ordinary commit, verified SSH signature, Co-authored-by maff0000 |
| Author and committer date | `2026-11-06T18:46:13Z` (18:46 Europe/London) |
| Accepted-head tree | `395fb0a8bad38476766cb24b5fe149ee91aab308` |
| Diff versus that parent | +193/−6 across exactly 2 files |
| Files in that diff, named only | `src/paperbots/native_recorder.py` +45/−4; `tests/test_native_recorder.py` +148/−2 |
| Acknowledgement fixture | `fixtures/native/wo008_offline/synthetic_offline_ack.txt` is not in that diff and was not rewritten |
| Private main and PR #12 base, unchanged | `d2c7fe9a4df8590488202e63dc3820480fd82546` |
| Private main message | `Merge PR #10 — WO-PAPER-007 native NEO communication readiness` |
| Private main parents | `28fe536e03ab8df1704d119b045158cc0a766f4f` and accepted WO-PAPER-007 design `8b27454eb2485f8fc3897e60d316b4bb11e4a885` |
| Private main tree | `75e4e07a049cb109f03ee3e5a11f133a71c5ebd5` |
| Compare versus that main | status ahead, ahead 4, behind 0, merge_base that same main SHA; 4 commits, +6835/−23 across 63 files |
| Private PR #12 body | Stale. It still names implementation commit `9851d0e` and 215 tests. Observation only. This record does not edit the private pull request |
| Prospective `merge_commit_sha` | If GitHub shows one on an open pull request, it is not a merge and is not recorded here |

## Ancestry versus private main

| Order | SHA | Parent | Message |
|---|---|---|---|
| 1 | `705477daf2bced29e6dbaae11c186dd12c3e1206` | `d2c7fe9a4df8590488202e63dc3820480fd82546` | `Propose WO-PAPER-008 offline native-message work order.` Accepted work-order SHA. Exact head of open private PR #11 |
| 2 | `9851d0e160a4dfe7aa2e29db23c92b0dc5e7b3fb` | `705477daf2bced29e6dbaae11c186dd12c3e1206` | `Implement WO-PAPER-008 offline native-message simulation.` Historical HOLD head |
| 3 | `05930fc35e40ee009c80bcaa4ecdca88b35c02ba` | `9851d0e160a4dfe7aa2e29db23c92b0dc5e7b3fb` | `Fail closed on unknown acknowledgement shapes.` Historical HOLD head |
| 4 | `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b` | `05930fc35e40ee009c80bcaa4ecdca88b35c02ba` | `Require a consistent synthetic dispatch before an acknowledgement.` Accepted implementation head |

The implementation branch was cut from `705477da` and did not add commits to private PR #11. An ordinary merge of PR #12 would include `705477da`. That is a later merge-order fact. It is not authority to merge either private pull request. This record does not perform that merge and does not invent its SHA.

## Earlier work-order acceptance

The earlier accepted work-order SHA remains `705477daf2bced29e6dbaae11c186dd12c3e1206`, recorded as REVIEW-M8-NEO-001 on open unmerged public [PR #15](https://github.com/maff0000/CGPT-INVESTMENT/pull/15), exact head `a9f5e9d301754dbf95095045d97fa5546431ed7a`, branch `cursor/wo-paper-008-architect-accept-792a`, base `573920e8a4deedb898917b41223fa6710a253695`. Public note, not recreated here: [WO-PAPER-008](https://github.com/maff0000/CGPT-INVESTMENT/blob/a9f5e9d301754dbf95095045d97fa5546431ed7a/work-orders/WO-PAPER-008-offline-native-message.md). Private [paper-bots PR #11](https://github.com/maff0000/paper-bots/pull/11) remains OPEN, not draft, not merged, still at that exact work-order head, 1 commit, +352/−0 across 5 documentation files, branch `cursor/wo-paper-008-offline-native-message-3e87`. Acceptance of that work-order SHA is not acceptance of the implementation. Acceptance of `c6cfcbb` is not a merge and is not closure.

## Historical HOLD heads

The Project Architect independently reviewed and ACCEPTED the implementation at exact private head `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b` on paper-bots PR #12. That acceptance supersedes the historical HOLD decisions for the earlier heads below. Those HOLD decisions remain preserved. They still apply to those earlier exact SHAs. There is no separate public HOLD review file for either earlier head. The HOLDs were Architect decisions recorded against those SHAs and are now historical. This record does not invent Git-tracked HOLD document IDs.

| Head | Architect status | Correction |
|---|---|---|
| `9851d0e160a4dfe7aa2e29db23c92b0dc5e7b3fb` | Historical HOLD | Ordinary commit `05930fc` failed closed on unknown acknowledgement shapes |
| `05930fc35e40ee009c80bcaa4ecdca88b35c02ba` | Historical HOLD | Ordinary commit `c6cfcbb` required a consistent synthetic dispatch before an acknowledgement and pinned the fixture SHA-256 |
| `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b` | ACCEPT | This record. Not a merge |

## Two resolved defects

Independent Architect review of held head `05930fc35e40ee009c80bcaa4ecdca88b35c02ba` identified one remaining blocking defect and one directly related fixture-integrity concern. The accepted head corrects both. The Architect verified that final correction. The Architect did not independently execute Python.

1. Acknowledgement required a corresponding accepted synthetic dispatch. Before recording a delivery acknowledgement, the recorder now requires the stored `PREPARED_REQUEST` and the corresponding `AUTHORISED_DISPATCH` for message `00700007-0007-4000-8000-000000000001`. An absent dispatch is `REJECT_HOLD` / `DISPATCH_ROW_REQUIRED`. If the stored dispatch message identity, basis, or disposition does not match the accepted synthetic dispatch, the result is `REJECT_HOLD` / `DISPATCH_INCONSISTENT`. Neither rejection appends a row or changes an existing one.
2. Acknowledgement fixture integrity required fixed SHA-256 verification. Admission now verifies SHA-256 `83286189711e629403b21673260e964d1550f3d3f7c104d045b4dccf25b52e70` of `fixtures/native/wo008_offline/synthetic_offline_ack.txt` before using those bytes as the reference. That digest is of the existing accepted fixture bytes, including the final newline. The file itself was not rewritten. A missing, unreadable, or modified file is `REJECT_HOLD` / `FIXTURE_INTEGRITY`. The labelled conflict variant (the fixture plus a final `conflict` line) remains `CONFLICT_HOLD` only when an acknowledgement row already exists and is not stored as an initial acknowledgement. Opaque acknowledgement bytes are not parsed into identity or authentication fields.

## Parent observation

The dispatch-consistency helper also requires the stored dispatch to keep `SENT_UNAUTHENTICATED` status, `live_message_sent` false, `platform_call.invoked` false, and the unauthenticated identity fields. There is no separate planted-row test for a wrong disposition alone. The parent did not treat this as a scope defect. This paragraph records that observation. It is not a new HOLD.

## Builder-reported tests

Builder-reported on the accepted head. Not independently executed by the Architect. Not independently executed by the parent. A passing simulation is not native authentication and is not Architect acceptance by itself.

```text
python3 --version
Python 3.12.3

PYTHONPATH=src python3 -m unittest discover -s tests -q
----------------------------------------------------------------------
Ran 223 tests in 3.011s

OK
```

Exit code 0. Previous builder-reported counts: 215 on `9851d0e160a4dfe7aa2e29db23c92b0dc5e7b3fb`; 218 on `05930fc35e40ee009c80bcaa4ecdca88b35c02ba`. The Architect did not independently execute Python.

## Named modules and unchanged protected files

Implementation modules and tests, named only: `src/paperbots/native_message.py`, `src/paperbots/native_evidence.py`, `src/paperbots/native_recorder.py`, narrow registration in `src/paperbots/schemautil.py`, catalog directory `docs/schemas/native-message-1/`, fixtures under `fixtures/native/wo008_offline/`, tests `tests/test_native_message.py`, `tests/test_native_evidence.py`, `tests/test_native_recorder.py`, `tests/test_native_review_response.py`, and `tests/wo008_support.py`. Their contents are not copied.

Protected private files remain unchanged by the implementation and both corrections: `src/paperbots/ledger.py`, `src/paperbots/native_ingest.py`, `src/paperbots/decision_evidence.py`, `docs/schemas/v0.3/catalog.json`, and QARP-ROTATION-001 v1.0.0. `send_native_message()` and `send_prepared_review_handoff()` still raise. No native message was sent. No second ledger. `Ledger.append_as` remains the only insertion route. `native-ledger-1` is not widened. The v0.3 catalog is not altered.

## Boundaries that remain unchanged

- `authenticates_sender` remains false
- `platform_attested_identity` remains `NOT_DOCUMENTED`
- `parent_platform_metadata` remains `REFUSED`
- Prepared row retains `PREPARED_NOT_SENT`
- `live_message_sent` remains false
- Prepared T-Bot → NEO handoff = NOT SENT
- QARP-ROTATION-001 v1.0.0 unchanged (file SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`; ruleset digest `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`)
- G0 remains OPEN
- Market-data provider rights remain UNVERIFIED
- Stop-dependent M/T remain HOLD
- Increment C isolation remains deferred
- No live broker, orders, strategy promotion, market-data provider calls, or trading activation

## Not authorised

- Merging private PR #11
- Merging private PR #12
- Merging public PR #15
- Merging this public pull request
- Sending the native message or the prepared T-Bot → NEO handoff
- Implementing or activating live transport
- Treating a claimed sender as authenticated
- Adding the deferred offline `check` command
- Changing QARP-ROTATION-001 v1.0.0, risk limits, trading authority, or historical evidence
- Deploying Increment C isolation
- Introducing a paid model API or starting the later v2 port
- Starting the new R-Bot optimisation task

When separately authorised later, merges must be ordinary merge commits only, with no squash, no rebase, and no rewriting of accepted source history. This record does not perform those merges and must not invent their SHAs. Record closure only after the relevant merges have actually occurred. This file is not a closure record.

## What remains open

Private PR #12 stays open and unmerged at `c6cfcbb97fc1255db89a579fd9b24c5901f55f5b`. Private PR #11 stays open and unmerged at `705477daf2bced29e6dbaae11c186dd12c3e1206`. Private main stays `d2c7fe9a4df8590488202e63dc3820480fd82546`. Public PR #15 stays open and unmerged at `a9f5e9d301754dbf95095045d97fa5546431ed7a`. Public main at this write stays `573920e8a4deedb898917b41223fa6710a253695`. This file names no future merge SHA.

Pointer files on this branch (`CURRENT-STATE.md`, `CHANGELOG.md`, `README.md`, `AGENTS.md`, `docs/adr/ADR-APP-002-bot-self-improvement.md`, `docs/equity-paper-delivery-roadmap.md`, and `work-orders/WO-PAPER-007-native-neo-communication.md`) overlap the same paths that public PR #15 also edits. This record does not hide that overlap by rebasing onto PR #15 or by rewriting PR #15. The proposed later merge order, which this session does not perform, is to merge public PR #15 first, then bring the then-current main into this branch by an ordinary merge, not a rebase of the accepted record.

This record does not send a native message or the prepared handoff. It does not add the deferred offline `check` command. It does not copy private Python, fixtures, tests, or schema catalog JSON.
