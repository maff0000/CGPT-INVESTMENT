# WO-PAPER-006 — synthetic NEO decision review (public note)

> **CURRENT — 6 November 2026. Architect HOLD of `619a607ed1879c93a82e4e652b2edc7531efb530`. Current head proposed, not accepted.** The Architect HOLDs that exact submitted head. No merge, live message, strategy promotion, or trading activation was authorised. The current proposal is exact head `4b3dac4c4137a5cb89a9587862e5fe25c464887b` on the same open private [paper-bots PR #9](https://github.com/maff0000/paper-bots/pull/9). Its parent `4078c6a560901ea67eb217f0486cdc18d045efa2` is the intermediate evidence-relationship correction. Authoritative packet: [REVIEW-M6-NEO-002](../research/reviews/2026-11-06-wo-paper-006-neo-review-correction-packet.md), which requests ACCEPT or HOLD of `4b3dac4c4137a5cb89a9587862e5fe25c464887b` and does not accept it. The historical request of the held head remains [REVIEW-M6-NEO-001](../research/reviews/2026-11-06-wo-paper-006-neo-review-packet.md). v0.3 stays explicitly synthetic: report `producer` `OFFLINE_DEMONSTRATOR`, `native_review_provenance` `NOT_APPROVED`. Builder-reported `Ran 162 tests` is not Architect acceptance. Generated proposals cite only findings present in the current review.

> **HISTORICAL REQUEST — 6 November 2026. Proposed at the time. Later held for `619a607`.** Private [paper-bots PR #9](https://github.com/maff0000/paper-bots/pull/9) exact head `619a607ed1879c93a82e4e652b2edc7531efb530` is parent-supplied OPEN, not draft, not merged. This public session could not open `maff0000/paper-bots`. Paper-bots main at open remains `c0b9f540c09caec08fb87e77bf445d0e580f843e`. Public `origin/main` before this note is `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. This note does not accept the private head and does not merge either pull request.

**Status:** PROPOSED for Architect ACCEPT or HOLD of exact private head `619a607ed1879c93a82e4e652b2edc7531efb530`. Not accepted. Not merged. That status line is the historical request of the held head. The current proposal is the successor section at the end of this note.
**Authoritative packet:** [REVIEW-M6-NEO-001](../research/reviews/2026-11-06-wo-paper-006-neo-review-packet.md), pinned to the head of `cursor/wo-paper-006-neo-review-packet-5d19`. The packet does not contain the SHA of the public commit that adds it.
**Public ADR:** [ADR-APP-002](../docs/adr/ADR-APP-002-bot-self-improvement.md)
**Predecessor:** [WO-PAPER-005](WO-PAPER-005-native-transport.md). Increment C design acceptance is [REVIEW-M5-INDEP-003](../research/reviews/2026-11-06-wo-paper-005-cf2dd5-independent-acceptance.md). That acceptance is design only. Isolation deployment remains deferred. The Increment A, B, and C text in the predecessor file is not rewritten by this note.
**Private pull request:** [paper-bots #9](https://github.com/maff0000/paper-bots/pull/9)
**Private work order path, not copied here:** `docs/work-orders/WO-PAPER-006-neo-decision-review.md`

## Parent-verified heads

This public session could not open `maff0000/paper-bots` (`gh pr view 9 --repo maff0000/paper-bots` returned `Could not resolve to a Repository`). The facts below are the parent's 6 Nov 2026 read-back. This note does not add private facts beyond that read-back. It does not record a prospective `merge_commit_sha`. If GitHub shows one on the open pull request, it is not a merge.

| Item | Value |
|---|---|
| Public `origin/main` before this note | `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` |
| Public main message | `Merge PR #12 — WO-PAPER-005 Increment C security-design acceptance` |
| Parents of that public main | `a962ba0019c6c4a19478dcf0e356ba58b07d61ff`, `d6fc7957613792478d3ea436bed616d409738113` |
| Private title | WO-PAPER-006 synthetic NEO review (proposed, not accepted) |
| Private branch | `cursor/wo-paper-006-neo-review-877f` |
| Private state | OPEN, not draft, not merged |
| Exact head | `619a607ed1879c93a82e4e652b2edc7531efb530` |
| Single parent, PR base, and paper-bots `main` | `c0b9f540c09caec08fb87e77bf445d0e580f843e` |
| Commits / diff | 1 commit, 25 files, +4437 / −1 |
| Author / author date / PR created | Cursor Agent, `2026-11-06T13:49:35Z`, PR created `2026-11-06T13:49:53Z` |
| Private commit message | Add WO-PAPER-006 synthetic NEO decision review. Record a v0.3 decision-evidence contract on the existing ledger, a planted six-Bot session, and an offline NEO review that separates decision quality from a later mark. The prepared T-Bot to NEO handoff is not sent. |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |

## What the increment is

A synthetic six-Bot decision session and the first example NEO review of it. E, S, R, M, and T emit structured decision evidence. An offline demonstrator applies a playbook written for the existing native NEO Bot and writes an example report. The demonstrator is labelled SYNTHETIC / OFFLINE and is not the native NEO Bot. No native message was sent.

Session `WO006-SYN-SESSION-001`. Correlation `00600006-0006-4000-8000-000000000001`. Market session `FIXTURE-2026-11-06`. Playbook `NEO-REVIEW-PLAYBOOK-v0.1`. Risk gate `NOT_INVOKED_NO_AUTHORITY`. Predictive performance `NOT_ASSESSED`.

## Planted findings

Parent-read review result. This session did not re-execute the review.

| ID | Class | What the review finds |
|---|---|---|
| `F-REASON-S-EARNINGS` | `REASONING_DOES_NOT_FOLLOW` | S-Bot asserts earnings_quality PASS; the input is FAIL |
| `F-REASON-S-MARGIN` | `REASONING_DOES_NOT_FOLLOW` | S-Bot asserts gross_margin_direction EXPANDING; the input is DETERIORATING |
| `F-MISSING-S-CONFIRMATION` | `MISSING_EVIDENCE` | S-Bot records STRATEGY_MATCH while independent_confirmation is ABSENT and the stated requirement is PRESENT |
| `F-BROKEN-M-CAUSAL` | `BROKEN_CAUSAL_REFERENCE` | M-Bot cites causal id `00600006-0006-4000-8000-000000000099`, which is not in the session |
| `F-INCONSISTENT-M-RBOT` | `CROSS_BOT_INCONSISTENCY` | M-Bot asserts R-Bot action PASS; R-Bot's decision is HOLD |
| `F-MISSING-M-SKEPTIC` | `MISSING_EVIDENCE` | M-Bot proposes PROPOSE_SHADOW_ENTRY and does not cite R-Bot's HOLD that blocked a new entry |
| `F-MISSED-S-WO006B` | `MISSED_OPPORTUNITY` | E-Bot recorded SYN-WO006B as meeting the stated threshold; S-Bot recorded no decision for it |
| `F-OUTCOME-M-MARK` | `FAVOURABLE_OUTCOME_POOR_DECISION` | A later synthetic mark moves SYN-WO006A from 100.00 SYN to 112.00 SYN; M-Bot quality stays POOR. The mark is not a fill |

Quality labels: E SOUND, S POOR, R SOUND, M POOR, T SOUND, NEO NOT_A_DECISION. A favourable mark does not upgrade a poor decision. A sound control stays sound when its mark is favourable.

## Contract decision

`native-ledger-1` stays as accepted. It drops `note` and writes a fixed explanation, so it cannot carry reasoning NEO can judge. v0.2 payloads are closed. ADR 0008 treats a payload change as a different decision. The new contract is schema v0.3, `decision-evidence-1`, on the same append-only ledger. There is no second ledger. Event types on this path: `DECISION_EVIDENCE` (E/S/R/M/T), `SYNTHETIC_OUTCOME_MARK` (T), `NEO_SESSION_REVIEW` (NEO), `IMPROVEMENT_PROPOSAL` (the Bot named `proposed_by`). Pre-existing role handles are not widened and cannot append these types or an order/fill. `authenticates_sender` stays false. `parent_platform_metadata` stays refused. `live_message_sent` stays false. Synthetic provenance is not authenticated native provenance.

The private schema catalog JSON is not copied into this repository. The parent-reported constant added in `src/paperbots/constants.py` is `SCHEMA_VERSION_V03 = "0.3.0"`. That source file is not copied here.

## Self-improvement requirement

Recorded verbatim. The canonical public ADR is [ADR-APP-002](../docs/adr/ADR-APP-002-bot-self-improvement.md). Recording it here does not accept the private head.

AGENT SELF-IMPROVEMENT — MANDATORY CAPABILITY

Every Bot must be capable of proposing improvements to its own prompts, analytical methods and strategies, informed by its experience, NEO's findings and collaboration with other Bots.

Improvements must be versioned and recorded in GitHub, with the original hypothesis, evidence, proposed change, evaluation results and rollback path.

Bots may autonomously develop and test experimental versions in offline or shadow mode. Their accepted versions remain unchanged until independently reviewed.

NEO must track performance by Bot, strategy and version, evaluate whether proposed improvements genuinely outperform their baselines, and recommend promotion or rejection.

NEO itself must be subject to evaluation and improvement.

No Bot may alter historical evidence, silently replace approved trading rules, increase authorised risk or activate live execution.

The common objective is sustainable, risk-controlled growth of the trading ledger through continuous, measurable improvement.

Sequence: NEO finding → proposed change → GitHub decision → bounded implementation → independent review → acceptance. A Bot may also start at the proposed change from its own experience, without waiting for NEO.

| Activity | Authority |
|---|---|
| Challenge another Bot's decision | Autonomous |
| Identify and explain mistakes | Autonomous |
| Research alternative methods | Autonomous |
| Propose strategy improvements | Autonomous |
| Create experimental Bot versions | Autonomous |
| Run offline/shadow comparisons | Autonomous |
| Recommend promotion of a better version | Autonomous |
| Replace an approved production strategy | Independent review required |
| Change risk limits or activate live trading | Explicit approval required |

This milestone records the table and stops at unevaluated proposals (`evaluation_status` `NOT_RUN`, `promotion` `NOT_RECOMMENDED`, `approved_strategy_replaced` false). It does not create an experimental Bot runtime or run a shadow comparison. Competing versions (for example S-Bot v1.0 vs v1.1) are a later roadmap item, not implemented here.

S-Bot files its own earnings-quality method proposal from Bot experience (experimental label `1.1-shadow-not-run`). The original `STRATEGY_MATCH` stays. QARP-ROTATION-001 v1.0.0 is not replaced. Applying a proposal raises and does not write the frozen manifest.

The financial performance ledger and the decision-evidence ledger stay distinct. Today both are different event types in the one append-only ledger. An outcome append does not update the decision row.

## Prepared handoff (not sent)

Named sender: T-Bot `81d8cf38-188e-4592-b08d-b59d6e461e83`.
Named recipient: NEO `e1e372c8-20e9-45a6-856f-4eabdf018308`.
Status: `PREPARED_NOT_SENT`. `live_message_sent` false. `authenticates_sender` false. `parent_platform_metadata` REFUSED. The send function raises and does not send.

Exact message text (the text that would later need named-principal authorisation):

```
T-Bot asks NEO to review synthetic offline session WO006-SYN-SESSION-001 under decision-evidence contract decision-evidence-1 and NEO review playbook NEO-REVIEW-PLAYBOOK-v0.1.

The session is fixture evidence for E-Bot, S-Bot, R-Bot, M-Bot, and T-Bot, plus one synthetic outcome mark. The mark is not an order and not a fill. Correlation 00600006-0006-4000-8000-000000000001. Market session FIXTURE-2026-11-06.

Report findings and a proposed improvement for each Bot. Keep decision quality separate from the later mark. Do not treat a favourable mark as a better decision. Do not promote a strategy. Do not change a risk limit. Do not activate trading. Do not replace QARP-ROTATION-001 v1.0.0.

This handoff is prepared only. It has not been sent. Sender identity is not authenticated. Synthetic provenance is not authenticated native provenance.
```

Later questions from NEO back to S-Bot or M-Bot are described, not prepared as sendable messages.

## Private names

Names and the parent-reported diff only. Contents are not copied. The parent-supplied diff is 25 files, +4437 / −1. ADR 0015 was not edited.

Added:

- `docs/work-orders/WO-PAPER-006-neo-decision-review.md`
- `docs/adr/0016-bot-self-improvement.md`
- `docs/roadmap/bot-self-improvement.md`
- `docs/contracts/decision-evidence-1.md`
- `docs/schemas/v0.3/README.md`
- `docs/schemas/v0.3/catalog.json`
- `docs/neo/NEO-REVIEW-PLAYBOOK-v0.1.md`
- `docs/reviews/2026-11-06-neo-wo006-synthetic.md`
- `examples/wo006_neo_session_review.json`
- `docs/handoffs/2026-11-06-tbot-to-neo-wo006-PREPARED-NOT-SENT.md`
- `fixtures/native/wo006_session/README.md`
- `fixtures/native/wo006_session/session.json`
- `src/paperbots/decision_evidence.py`
- `tests/test_decision_evidence.py`

Modified (pointer / catalog / docstring only, except the new modules above):

- `README.md`, `RUNBOOK.md`
- `docs/adr/0010-native-role-contract.md` (+2)
- `docs/adr/0012-native-ledger-ingest.md` (+2)
- `docs/schemas/v0.2/README.md` (+2)
- `docs/work-orders/WO-PAPER-005-native-transport.md` (+4 successor paragraph only; no deletions of Increment A/B/C text)
- `fixtures/README.md` (+1)
- `src/paperbots/constants.py` (adds `SCHEMA_VERSION_V03 = "0.3.0"`)
- `src/paperbots/native_contract.py`
- `src/paperbots/schemautil.py`
- `src/paperbots/neo_report.py` (module docstring only: it is not the native NEO Bot and does not apply this playbook)

## Builder tests

The parent reviewed published documents and tests through GitHub and did not re-execute the suite. This public session did not run it.

The private builder reported `PYTHONPATH=src python3 -m unittest discover -s tests -q` on Python 3.12.3: `Ran 161 tests`, `OK`, exit 0. The 161 includes the previous 152. Python 3.9 was not installed there. **Builder 161 is not Architect acceptance.**

The parent read the work order, ADR 0016, the playbook, the example review, the contract note, the prepared handoff, the planted-session README, and the new tests. The tests lock: the eight planted findings; quality independent of the mark; rejection of `authenticates_sender` true / `parent_platform_metadata` / trading permission / a replaced strategy version; append-only ingest and replay; no silent QARP replacement; closed pre-existing role allowlists; named unsent handoff; committed report matches a fresh review. No private test method name is copied here.

## Exclusions

No merge. No acceptance of the private head by this note. No live native message. No Cursor user, OS account, credential, scheduler, broker or account read, vendor call, order, or fill. No new strategy risk parameter. No replacement of QARP-ROTATION-001 v1.0.0. No experimental Bot runtime. No shadow comparison. No deployment of Increment C isolation.

G0 stays OPEN. Provider rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. No fourth call. Stop-dependent M/T stays HOLD.

## Requested next step

Architect independent review of exact private head `619a607ed1879c93a82e4e652b2edc7531efb530`, then ACCEPT or HOLD on that head. Acceptance would record the synthetic review and this requirement. It would not send the handoff, would not replace QARP-ROTATION-001 v1.0.0, would not authenticate a sender, would not deploy Increment C isolation, and would not create an experimental runtime. This note is the handoff. It is not the decision.

## Successor — current head after the Architect HOLD, proposed, not accepted

**Status:** The Architect HOLDs `619a607ed1879c93a82e4e652b2edc7531efb530`. The current proposal is exact head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. Not accepted. Not merged.
**Authoritative packet:** [REVIEW-M6-NEO-002](../research/reviews/2026-11-06-wo-paper-006-neo-review-correction-packet.md)
**Historical request:** the sections above, and [REVIEW-M6-NEO-001](../research/reviews/2026-11-06-wo-paper-006-neo-review-packet.md)

The sections above stay. They are the request the Architect held. Private PR #9 remains OPEN, not draft, not merged, on paper-bots main `c0b9f540c09caec08fb87e77bf445d0e580f843e`. This public session could not open the private repository. No private source is copied. No prospective merge-commit SHA is recorded.

`4078c6a560901ea67eb217f0486cdc18d045efa2` is the intermediate correction. Its parent is the held head. Author Cursor Agent. Message: `Correct WO-PAPER-006 evidence relationships after Architect hold.` Diff versus the held head: 10 files, +410/−46. That commit is ancestry. It is not the head under review. On that ancestry, an outcome must match the referenced decision's instrument, session, correlation, and market session, and the mark label must agree with the numerical direction. A later positive action after a blocking HOLD is `HOLD_VIOLATED` whether or not the HOLD is cited. The planted session keeps `F-MISSING-M-SKEPTIC` and adds `F-HOLD-M-RBOT`. The original eight findings remain. `STRATEGY_MATCH` and `PROPOSE_SHADOW_ENTRY` must use frozen QARP-ROTATION-001 v1.0.0. Another strategy id does not skip the pin. Proposal evidence references must resolve. Duplicate logical evidence ids are rejected. v0.3 report `producer` is `OFFLINE_DEMONSTRATOR` and `native_review_provenance` is `NOT_APPROVED`.

The current head is `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. Its parent is `4078c6a560901ea67eb217f0486cdc18d045efa2`. Author Cursor Agent, author date `2026-11-06T14:24:49Z`. Message: `Cite only findings present when NEO drafts a proposal.` Diff versus that parent: 3 files, +28/−7, named only as `src/paperbots/decision_evidence.py`, `tests/test_decision_evidence.py`, and the private work order. The whole private PR versus paper-bots main is 3 commits, 25 files, +4822/−1. Generated NEO proposals cite only finding ids present in the current review. `informed_by_neo_finding` is true only when at least one such finding remains. A valid unfavourable flip of the planted mark from 100.00 SYN to 90.00 SYN still reviews: M-Bot stays POOR, `F-OUTCOME-M-MARK` is absent, and no generated proposal names it. Correcting S-Bot's reasoning claims so they match the inputs removes `F-REASON-S-EARNINGS` and `F-REASON-S-MARGIN`. The review completes. `F-MISSING-S-CONFIRMATION` and `F-HOLD-M-RBOT` remain. Generated proposals do not keep the dropped finding ids. A session-supplied proposal that names `F-NOT-IN-THIS-REVIEW` is rejected before any ledger append. A fabricated proposal evidence id is rejected the same way.

Builder report on this head, not re-executed: Python 3.12.3 `Ran 162 tests`, `OK`, exit 0. `PYTHONPATH=src python3 -m paperbots.decision_evidence check` reported `SYNTHETIC_OFFLINE findings 9` and the nine planted ids, and sent nothing. GitHub reports no CI status checks. Builder 162 is not Architect acceptance. QARP file SHA-256 and ruleset digest are unchanged. `authenticates_sender` stays false. `parent_platform_metadata` stays refused. No live message was sent.

Requested next step: Architect ACCEPT or HOLD of exact head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. The HOLD of `619a607ed1879c93a82e4e652b2edc7531efb530` stays the decision for that older head. This section does not accept `4b3dac4c4137a5cb89a9587862e5fe25c464887b` and does not request a disposition of the intermediate parent.
