# WO-PAPER-006 — correction after Architect HOLD

**ID:** REVIEW-M6-NEO-002
**Date:** 2026-11-06 (Europe/London)
**Record type:** public governance packet for the current head of the open private pull request.
**Disposition requested:** Architect **ACCEPT or HOLD** of exact current head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`.
**This packet does not accept that head.** It does not merge private [paper-bots PR #9](https://github.com/maff0000/paper-bots/pull/9) or public [PR #13](https://github.com/maff0000/CGPT-INVESTMENT/pull/13). It does not send a message. It does not copy private Python, tests, fixtures, or schema catalog JSON. Builder-reported `Ran 162 tests` is not Architect acceptance. The parent did not re-execute the suite. This public session did not run it.

The Architect HOLDs exact submitted head `619a607ed1879c93a82e4e652b2edc7531efb530`. That HOLD is valid for that head. [REVIEW-M6-NEO-001](2026-11-06-wo-paper-006-neo-review-packet.md) remains the historical request of that head and is not rewritten as if the request never happened. `4078c6a560901ea67eb217f0486cdc18d045efa2` is the intermediate evidence-relationship correction. It is the parent of the current head. It is not the head under review.

Accepted Increment C stays accepted as a design only, with no deployment. [REVIEW-M5-INDEP-003](2026-11-06-wo-paper-005-cf2dd5-independent-acceptance.md) records that acceptance. Increment C isolation deployment remains deferred. Historical REVIEW-M5 files are not edited here. Merged public [PR #10](https://github.com/maff0000/CGPT-INVESTMENT/pull/10), [PR #11](https://github.com/maff0000/CGPT-INVESTMENT/pull/11), and [PR #12](https://github.com/maff0000/CGPT-INVESTMENT/pull/12) are closed history and are not reused.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-006-neo-review-packet-5d19` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | Public branch `cursor/wo-paper-006-neo-review-packet-5d19` head `1c6c1423d05e62c52a73a6b37e62cb43b4ca2d9c`, parent `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. `git fetch` returned the same branch head and the same `origin/main`. That branch head is the parent of this public commit. `gh pr view 9 --repo maff0000/paper-bots` returned `Could not resolve to a Repository`. This session did not read private blobs |
| Parent-supplied private read-back, 6 Nov 2026 | The Architect HOLD of `619a607`, the safeguards the Architect treated as preserved, the six correction findings, the intermediate head `4078c6a`, the current head `4b3dac4`, its parent, author date, message, diff sizes, named paths, the parent's reading of both commits, and the builder report on the current head |
| Not claimed here | Architect acceptance of `4b3dac4`, a request to accept or hold `4078c6a` as the current head, withdrawal of the HOLD of `619a607`, a merge, a prospective merge-commit SHA, a re-run of the 162 tests, sender authentication, a live message, strategy promotion, trading activation, vendor rights, or a fourth FMP call |

This public session did not copy private Python, tests, fixture JSON, or schema catalog JSON. Private facts below are the parent read-back. Naming a private path or SHA is not a copy of its contents. No private test method name is invented here.

## Architect HOLD of `619a607`

The Architect independently reviewed private paper-bots PR #9 at exact submitted head `619a607ed1879c93a82e4e652b2edc7531efb530` and HOLDs acceptance pending a bounded correction. No merge, live messaging, strategy promotion, or trading activation was authorised.

The architecture direction and these safeguards were accepted as preserved:

- The existing append-only ledger stays.
- Historical v0.1 and v0.2 stay unchanged.
- The synthetic 100.00 SYN to 112.00 SYN mark is not a trade or a fill.
- The NEO review does not alter historical decisions.
- S-Bot can propose without replacing the approved strategy.
- The T-Bot to NEO handoff stays prepared and unsent.
- Trading authority, risk-limit changes, and strategy promotion remain prohibited.

Findings that required correction:

1. P1. Outcome-to-decision linkage was incomplete: a synthetic outcome could reference a decision for a different instrument.
2. P1. HOLD could be acknowledged but still violated: citing a veto did not keep the blocker finding.
3. P1. Frozen strategy identity could be bypassed: the pin applied when the strategy id equalled QARP-ROTATION-001.
4. P2. Proposal evidence references were insufficiently validated.
5. P2. Native NEO contract needed clarification: v0.3 must stay explicitly synthetic. A future genuine native review needs a separately approved provenance representation and must not masquerade as the offline demonstrator.
6. A further outcome check: the favourable or unfavourable label must agree with the numerical direction of the mark. A fall from 100 to 90 must not be labelled favourable.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main`, unchanged | `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` |
| Public PR | [CGPT-INVESTMENT #13](https://github.com/maff0000/CGPT-INVESTMENT/pull/13) |
| Public PR head before this write, and parent of this public commit | `1c6c1423d05e62c52a73a6b37e62cb43b4ca2d9c` |
| Public branch | `cursor/wo-paper-006-neo-review-packet-5d19` |
| Historical public packet | [REVIEW-M6-NEO-001](2026-11-06-wo-paper-006-neo-review-packet.md) |
| Private pull request | [paper-bots #9](https://github.com/maff0000/paper-bots/pull/9) |
| Private state | OPEN, not draft, not merged |
| Held private head | `619a607ed1879c93a82e4e652b2edc7531efb530` |
| Intermediate correction | `4078c6a560901ea67eb217f0486cdc18d045efa2` |
| Parent of that intermediate commit | `619a607ed1879c93a82e4e652b2edc7531efb530` |
| Intermediate message | `Correct WO-PAPER-006 evidence relationships after Architect hold.` |
| Intermediate diff versus the held head | 10 files, +410 / −46 |
| Private head under review | `4b3dac4c4137a5cb89a9587862e5fe25c464887b` |
| Parent of the current head | `4078c6a560901ea67eb217f0486cdc18d045efa2` |
| Current-head author / author date | Cursor Agent, `2026-11-06T14:24:49Z` |
| Current-head message | `Cite only findings present when NEO drafts a proposal.` |
| Current-head diff versus `4078c6a` | 3 files, +28 / −7 |
| Whole private PR versus paper-bots main | 3 commits, 25 files, +4822 / −1 |
| Paper-bots main and PR base | `c0b9f540c09caec08fb87e77bf445d0e580f843e` |
| GitHub `merge_commit_sha` | Not quoted by the parent read-back and not recorded here. If GitHub shows one, it is not a merge |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |

## What `4078c6a` implemented

Parent-read ancestry. This commit is not the head under review.

An outcome must match the referenced decision's `instrument_id`, `session_id`, `correlation_id`, and `market_session`. Observation must be later than the referenced decision. A favourable label must be a rising mark. An unfavourable label must be a falling mark. These checks run before any ledger append.

A later positive action after a blocking HOLD is recorded as `HOLD_VIOLATED` whether or not that HOLD is cited. The planted session still has `F-MISSING-M-SKEPTIC` and also `F-HOLD-M-RBOT`.

`STRATEGY_MATCH` and `PROPOSE_SHADOW_ENTRY` must use frozen QARP-ROTATION-001 v1.0.0. Another strategy id does not skip the pin.

Duplicate logical evidence ids are rejected. Proposal `evidence_ids` and `evidence_finding_ids` must resolve.

The v0.3 report `producer` is `OFFLINE_DEMONSTRATOR` and `native_review_provenance` is `NOT_APPROVED`.

The original eight planted findings remain. `F-HOLD-M-RBOT` / `HOLD_VIOLATED` is added.

## What `4b3dac4` added

Parent-read behaviour of the current head, not an Architect confirmation.

Generated NEO proposals cite only finding ids present in the current review. `informed_by_neo_finding` is true only when at least one such finding remains.

Flipping the planted mark to a valid unfavourable 100.00 to 90.00 still reviews. M-Bot stays POOR. `F-OUTCOME-M-MARK` is absent. No generated NEO proposal names it.

Correcting S-Bot's reasoning claims so they match the inputs removes `F-REASON-S-EARNINGS` and `F-REASON-S-MARGIN`. The review completes. Findings that do not depend on those claims remain, including `F-MISSING-S-CONFIRMATION` and `F-HOLD-M-RBOT`. Generated proposals do not keep the dropped finding ids.

A session-supplied proposal that names a finding id that is not in the review (`F-NOT-IN-THIS-REVIEW`) is still rejected before any ledger append. A fabricated proposal evidence id is still rejected the same way.

## Private names on the current head

Names and the parent-reported diff only. Contents are not copied. The current head versus `4078c6a` is 3 files, +28 / −7.

- `src/paperbots/decision_evidence.py`
- `tests/test_decision_evidence.py`
- `docs/work-orders/WO-PAPER-006-neo-decision-review.md`

## Tests

Parent-supplied builder report on `4b3dac4`. The parent did not re-execute the suite. This public session did not run it. GitHub reports no CI status checks.

Python 3.12.3, command `PYTHONPATH=src python3 -m unittest discover -s tests -q`, reported `Ran 162 tests`, `OK`, exit 0. The same environment's `PYTHONPATH=src python3 -m paperbots.decision_evidence check` reported `SYNTHETIC_OFFLINE findings 9` and the nine planted ids, and sent nothing. **Builder 162 is not Architect acceptance.**

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, broker or account read, vendor call, or trade-policy approval is granted.
- No bot message was sent. `authenticates_sender` stays false. `parent_platform_metadata` stays refused.
- QARP-ROTATION-001 v1.0.0 is not replaced.
- v0.3 stays an offline demonstrator. `native_review_provenance` stays `NOT_APPROVED`.

## Limitations

- The HOLD of `619a607ed1879c93a82e4e652b2edc7531efb530` stands for that exact head.
- `4078c6a560901ea67eb217f0486cdc18d045efa2` is ancestry. This packet does not request a disposition of that intermediate SHA.
- The current head is proposed. This packet does not accept it.
- The offline demonstrator is not a genuine native NEO review.
- The prepared handoff was not sent.
- This session did not open `maff0000/paper-bots` and did not re-run the 162 tests or the check command.
- Increment C isolation remains deferred.

## Restrictions

This packet authorises none of the following:

- acceptance of `4b3dac4c4137a5cb89a9587862e5fe25c464887b`
- treating `4078c6a560901ea67eb217f0486cdc18d045efa2` as the current private head
- withdrawal of the HOLD of `619a607ed1879c93a82e4e652b2edc7531efb530`
- merge of private PR #9 or of public PR #13
- a live native message, strategy promotion, or trading activation
- a risk-limit change or replacement of QARP-ROTATION-001 v1.0.0
- presentation of the offline demonstrator as a genuine native review
- `authenticates_sender` true, or `parent_platform_metadata` as proof of identity
- a fourth FMP call, a scheduler, a broker or account read, or an order or fill
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect review of exact current head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`, then an **ACCEPT** or **HOLD** recorded against that SHA. The HOLD of `619a607ed1879c93a82e4e652b2edc7531efb530` stays the decision for that older head. Acceptance of the current head would record the evidence-relationship checks in its ancestry and the rule that a generated proposal cites only findings present in the current review. It would not send the handoff, would not replace an approved strategy, would not authenticate a sender, and would not activate trading. Until that independent review exists, the current head stays proposed.

Rollback of an unaccepted head is to leave paper-bots main at `c0b9f540c09caec08fb87e77bf445d0e580f843e` and public main at `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. This file does not perform either merge.
